from flask import Blueprint, request, jsonify, make_response
from models.respuesta import Respuesta
from utils.db import db
from schemas.respuesta_schema import respuesta_schema, respuestas_schema
from flask_jwt_extended import jwt_required

respuestas = Blueprint('respuestas', __name__)

@respuestas.route('/respuestas/get', methods=['GET'])
@jwt_required()
def get_respuestas():
    result = {}
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
    id_pregunta = data.get('id_pregunta')
    id_alternativa = data.get('id_alternativa')
    
    if id_test==None or id_pregunta==None or id_alternativa==None:
        data = {
            'message': 'Faltan datos',
            'status': 400
        }
        
        return make_response(jsonify(data), 400)
    
    respuesta = Respuesta(id_test, id_pregunta, id_alternativa)
    db.session.add(respuesta)
    db.session.commit()
    
    data = {
        'message': 'Respuesta creada con éxito',
        'status': 201,
        'data': respuesta_schema.dump(respuesta)
    }
    
    return make_response(jsonify(data), 201)

# LA FUNCIÓN UPDATE NO SERÁ IMPLEMENTADA EN EL FRONTEND
@respuestas.route('/respuestas/update/<int:id_respuesta>', methods=['PUT'])
@jwt_required()
def update(id_respuesta):
    respuesta = Respuesta.query.get(id_respuesta)
    
    if respuesta == None:
        data = {
            'message': 'No se encontró la respuesta',
            'status': 404
        }
        
        return make_response(jsonify(data), 404)
    
    respuesta.id_test = request.json.get('id_test')
    respuesta.id_pregunta = request.json.get('id_pregunta')
    respuesta.id_alternativa = request.json.get('id_alternativa')
    
    db.session.commit()
    
    data = {
        'message': 'Respuesta actualizada con éxito',
        'status': 200,
        'data': respuesta_schema.dump(respuesta)
    }
    
    return make_response(jsonify(data), 200)
    
@respuestas.route('/respuestas/delete/<int:id_alternativa>', methods=['DELETE'])
@jwt_required()
def delete(id_alternativa):
    respuesta = Respuesta.query.get(id_alternativa)
    
    if respuesta == None:
        data = {
            'message': 'Respuesta no encontrada',
            'status': 404
        }
        
        return make_response(jsonify(data), 404)
    
    db.session.delete(respuesta)
    
    data = {
        'message': 'Respuesta eliminada con éxito',
        'status': 200,
        'data': respuesta_schema.dump(respuesta)
    }
    
    return make_response(jsonify(data), 200)