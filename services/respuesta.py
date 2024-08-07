from schemas.respuesta_schema import respuesta_schema, respuestas_schema
from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import jwt_required
from models.respuesta import Respuesta
from utils.db import db

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

@respuestas.route('/respuestas/get/<int:id_test>', methods=['GET'])
@jwt_required()
def get_respuestas_test(id_test):
    result = {}
    respuestas = Respuesta.query.filter_by(id_test=id_test).all()
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
    marcadas = data.get('marcadas')
    
    if id_test==None or marcadas==None:
        data = {
            'message': 'Faltan datos',
            'status': 400
        }
        
        return make_response(jsonify(data), 400)
    
    for marcada in marcadas:
        respuesta = Respuesta(id_test, marcada['id_pregunta'], marcada['id_alternativa'])
        db.session.add(respuesta)
    
    db.session.commit()
    
    result = {
        "message": "Respuestas creadas con éxito",
        "status": 201,
        "respuestas": data
    }
    
    return make_response(jsonify(result), 201)

@respuestas.route('/respuestas/update/<int:id_respuesta>', methods=['PUT'])
@jwt_required()
def update(id_respuesta):
    respuesta = Respuesta.query.get(id_respuesta)
    
    if not respuesta:
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
        'respuesta': respuesta_schema.dump(respuesta)
    }
    
    return make_response(jsonify(data), 200)
    
@respuestas.route('/respuestas/delete/<int:id_respuesta>', methods=['DELETE'])
@jwt_required()
def delete(id_respuesta):
    respuesta = Respuesta.query.get(id_respuesta)
    
    if not respuesta:
        data = {
            'message': 'Respuesta no encontrada',
            'status': 404
        }
        
        return make_response(jsonify(data), 404)

    db.session.delete(respuesta)
    
    db.session.commit()
    
    data = {
        'message': 'Respuesta eliminada con éxito',
        'status': 200
    }
    
    return make_response(jsonify(data), 200)