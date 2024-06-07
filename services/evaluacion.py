from flask import Blueprint, request, jsonify, make_response
from models.evaluacion import Evaluacion
from utils.db import db
from schemas.evaluacion_schema import evaluacion_schema, evaluaciones_schema
from flask_jwt_extended import jwt_required

evaluaciones = Blueprint('evaluaciones', __name__)

@evaluaciones.route('/evaluaciones/get', methods=['GET'])
@jwt_required()
def get_evaluaciones():
    evaluaciones = Evaluacion.query.all()
    result = evaluaciones_schema.dump(evaluaciones)
    
    data = {
        'message': 'Lista generada con éxito',
        'status': 200,
        'evaluaciones': result
    }
    
    return make_response(jsonify(data), 200)

@evaluaciones.route('/evaluaciones/insert', methods=['POST'])
@jwt_required()
def insert():
    data = request.get_json()
    id_historial_clinico = data.get('id_historial_clinico')
    fecha = data.get('fecha')
    estado = data.get('estado')
    tratamiento = data.get('tratamiento')
    
    if not id_historial_clinico or not estado or not tratamiento:
        data = {
            'message': 'Faltan datos',
            'status': 400
        }
        
        return make_response(jsonify(data), 400)
    
    new_evaluacion = Evaluacion(id_historial_clinico, fecha, estado, tratamiento)
    db.session.add(new_evaluacion)
    db.session.commit()
    
    result = evaluacion_schema.dump(new_evaluacion)
    
    data = {
        'message': 'Evaluacion creada con éxito',
        'status': 201,
        'data': result
    }
    
    return make_response(jsonify(result), 201)

@evaluaciones.route('/evaluaciones/update/<int:id>', methods=['PUT'])
@jwt_required()
def update(id):
    data = request.get_json()
    evaluacion = Evaluacion.query.get(id)
    
    if evaluacion:
        evaluacion.id_historial_clinico = data.get('id_historial_clinico')
        evaluacion.fecha = data.get('fecha')
        evaluacion.estado = data.get('estado')
        evaluacion.tratamiento = data.get('tratamiento')
        
        db.session.commit()
        
        result = evaluacion_schema.dump(evaluacion)
        
        data = {
            'message': 'Evaluacion actualizada con éxito',
            'status': 200,
            'data': result
        }
        
        return make_response(jsonify(data), 200)
        
    data = {
        'message': 'No se encontró la evaluacion',
        'status': 404
    }
        
    return make_response(jsonify(data), 404)

@evaluaciones.route('/evaluaciones/delete/<int:id>', methods=['DELETE'])
@jwt_required()
def delete(id):
    evaluacion = Evaluacion.query.get(id)
    
    if evaluacion:
        db.session.delete(evaluacion)
        db.session.commit()
        
        data = {
            'message': 'Evaluacion eliminada con éxito',
            'status': 200,
        }
        
        return make_response(jsonify(data), 200)
    
    data = {
            'message': 'No se encontró la evaluacion',
            'status': 404
        }
        
    return make_response(jsonify(data), 404)

