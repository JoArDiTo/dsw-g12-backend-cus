from flask import Blueprint, request, jsonify, make_response
from models.escala_calificacion import EscalaCalificacion
from utils.db import db
from schemas.escala_calificacion_schema import escala_calificacion_schema, escalas_calificacion_schema
from flask_jwt_extended import jwt_required

escalas = Blueprint('escalas', __name__)

@escalas.route('/escalas/get', methods=['GET'])
@jwt_required()
def get_escalas_calificacion():
    escalas_calificacion = EscalaCalificacion.query.all()
    result = escalas_calificacion_schema.dump(escalas_calificacion)
    
    data = {
        'message': 'Lista generada con éxito',
        'status': 200,
        'escalas_calificacion': result
    }

    return make_response(jsonify(data), 200)

@escalas.route('/escalas/insert', methods=['POST'])
@jwt_required()
def insert():
    data = request.get_json()
    id_tipo_test = data.get('id_tipo_test')
    descripcion = data.get('descripcion')
    
    if not id_tipo_test or not descripcion:
        data = {
            'message': 'Faltan datos',
            'status': 400
        }
        
        return make_response(jsonify(data), 400)
    
    escala_calificacion = EscalaCalificacion(id_tipo_test, descripcion)
    db.session.add(escala_calificacion)
    db.session.commit()
    
    result = escala_calificacion_schema.dump(escala_calificacion)
    
    data = {
        'message': 'Escala de calificación creada con éxito',
        'status': 201,
        'data': result
    }
    
    return make_response(jsonify(result), 201)

@escalas.route('/escalas/update/<int:id>', methods=['PUT'])
@jwt_required()
def update(id):
    data = request.get_json()
    escala_calificacion = EscalaCalificacion.query.get(id)
    
    if escala_calificacion:
        escala_calificacion.id_tipo_test = data.get('id_tipo_test')
        escala_calificacion.descripcion = data.get('descripcion')
        db.session.commit()
        
        result = escala_calificacion_schema.dump(escala_calificacion)
        
        data = {
            'message': 'Escala de calificación actualizada con éxito',
            'status': 200,
            'data': result
        }
        
        return make_response(jsonify(data), 200)
    
    data = {
        'message': 'Escala de calificación no encontrada',
        'status': 404
    }
    
    return make_response(jsonify(data), 404)

@escalas.route('/escalas/delete/<int:id>', methods=['DELETE'])
@jwt_required()
def delete(id):
    escala_calificacion = EscalaCalificacion.query.get(id)
    
    if escala_calificacion:
        db.session.delete(escala_calificacion)
        db.session.commit()
        
        data = {
            'message': 'Escala de calificación eliminada con éxito',
            'status': 200
        }
        
        return make_response(jsonify(data), 200)
    
    data = {
        'message': 'Escala de calificación no encontrada',
        'status': 404
    }
    
    return make_response(jsonify(data), 404)
    
