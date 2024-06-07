from flask import Blueprint, request, jsonify, make_response
from models.rango_calificacion import RangoCalificacion
from utils.db import db
from schemas.rango_calificacion_schema import rango_calificacion_schema, rangos_calificacion_schema
from flask_jwt_extended import jwt_required

rangos = Blueprint('rangos', __name__)

@rangos.route('/rangos/get', methods=['GET'])
@jwt_required()
def get_rangos_calificacion():
    rangos_calificacion = RangoCalificacion.query.all()
    result = rangos_calificacion_schema.dump(rangos_calificacion)
    
    data = {
        'message': 'Lista generada con éxito',
        'status': 200,
        'rangos_calificacion': result
    }
    
    return make_response(jsonify(data), 200)

@rangos.route('/rangos/insert', methods=['POST'])
@jwt_required()
def insert():
    data = request.get_json()
    id_escala_calificacion = data.get('id_escala_calificacion')
    puntaje_min = data.get('puntaje_min')
    puntaje_max = data.get('puntaje_max')
    interpretacion = data.get('interpretacion')
    
    if not id_escala_calificacion or not puntaje_min or not puntaje_max or not interpretacion:
        data = {
            'message': 'Faltan datos',
            'status': 400
        }
        
        return make_response(jsonify(data), 400)

    rango_calificacion = RangoCalificacion(id_escala_calificacion, puntaje_min, puntaje_max, interpretacion)    
    db.session.add(rango_calificacion)
    db.session.commit()
    
    result = rango_calificacion_schema.dump(rango_calificacion)
    
    data = {
        'message': 'Rango de calificación creado con éxito',
        'status': 201,
        'data': result
    }
    
    return make_response(jsonify(result), 201)

@rangos.route('/rangos/update/<int:id>', methods=['PUT'])
@jwt_required()
def update(id):
    data = request.get_json()
    rango_calificacion = RangoCalificacion.query.get(id)
    
    if rango_calificacion:
        rango_calificacion.id_escala_calificacion = data.get('id_escala_calificacion')
        rango_calificacion.puntaje_min = data.get('puntaje_min')
        rango_calificacion.puntaje_max = data.get('puntaje_max')
        rango_calificacion.interpretacion = data.get('interpretacion')
        db.session.commit()
        
        result = rango_calificacion_schema.dump(rango_calificacion)
        
        data = {
            'message': 'Rango de calificación actualizado con éxito',
            'status': 200,
            'data': result
        }
        
        return make_response(jsonify(data), 200)
    
    data = {
        'message': 'Rango de calificación no encontrado',
        'status': 404
    }
    
    return make_response(jsonify(data), 404)

@rangos.route('/rangos/delete/<int:id>', methods=['DELETE'])
@jwt_required()
def delete(id):
    rango_calificacion = RangoCalificacion.query.get(id)
    
    if rango_calificacion:
        db.session.delete(rango_calificacion)
        db.session.commit()
        
        data = {
            'message': 'Rango de calificación eliminado con éxito',
            'status': 200
        }
        
        return make_response(jsonify(data), 200)
    
    data = {
        'message': 'Rango de calificación no encontrado',
        'status': 404
    }
    
    return make_response(jsonify(data), 404)