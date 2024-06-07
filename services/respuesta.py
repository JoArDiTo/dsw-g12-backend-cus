from flask import Blueprint, request, jsonify, make_response
from models.respuesta import Respuesta
from utils.db import db
from schemas.respuesta_schema import respuesta_schema, respuestas_schema
from flask_jwt_extended import jwt_required

respuestas = Blueprint('respuestas', __name__)

@respuestas.route('/respuestas/get', methods=['GET'])
@jwt_required()
def get_respuestas():
    respuestas = Respuesta.query.all()
    result = respuestas_schema.dump(respuestas)
    
    data = {
        'message': 'Lista generada con éxito',
        'status': 200,
        'respuestas': result
    }

    return make_response(jsonify(data), 200)

@respuestas.route('/respuestas/insert', methods=['POST'])
@jwt_required()
def insert():
    data = request.get_json()
    id_test = data.get('id_test')
    pregunta = data.get('pregunta')
    respuesta = data.get('respuesta')
    puntaje = data.get('puntaje')
    
    if not id_test or not pregunta or not respuesta or not puntaje:
        data = {
            'message': 'Faltan datos',
            'status': 400
        }
        
        return make_response(jsonify(data), 400)
    
    respuesta = Respuesta(id_test, pregunta, respuesta, puntaje)
    db.session.add(respuesta)
    db.session.commit()
    
    result = respuesta_schema.dump(respuesta)
    
    data = {
        'message': 'Respuesta creada con éxito',
        'status': 201,
        'data': result
    }
    
    return make_response(jsonify(result), 201)

@respuestas.route('/respuestas/update/<int:id>', methods=['PUT'])
@jwt_required()
def update(id):
    data = request.get_json()
    respuesta = Respuesta.query.get(id)
    
    if respuesta:
        respuesta.id_test = data.get('id_test')
        respuesta.pregunta = data.get('pregunta')
        respuesta.respuesta = data.get('respuesta')
        respuesta.puntaje = data.get('puntaje')
        db.session.commit()
        
        result = respuesta_schema.dump(respuesta)
        
        data = {
            'message': 'Respuesta actualizada con éxito',
            'status': 200,
            'data': result
        }
        
        return make_response(jsonify(data), 200)
    
    data = {
        'message': 'Respuesta no encontrada',
        'status': 404
    }
    
    return make_response(jsonify(data), 404)

#UNA RESPUESTA NO PUEDE SER BORRADA, DEBIDO A QUE QUEDA REGISTRADA

@respuestas.route('/respuestas/delete/<int:id>', methods=['DELETE'])
@jwt_required()
def delete(id):
    respuesta = Respuesta.query.get(id)
    
    if respuesta:
        db.session.delete(respuesta)
        db.session.commit()
        
        data = {
            'message': 'Respuesta eliminada con éxito',
            'status': 200
        }
        
        return make_response(jsonify(data), 200)
    
    data = {
        'message': 'No se encontró la respuesta',
        'status': 404
    }
    
    return make_response(jsonify(data), 404)