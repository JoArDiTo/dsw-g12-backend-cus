from schemas.pregunta_schema import pregunta_schema, preguntas_schema
from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import jwt_required
from models.pregunta import Pregunta
from utils.db import db

preguntas = Blueprint('preguntas', __name__)

@preguntas.route('/preguntas/get', methods=['GET'])
@jwt_required()
def get_preguntas():
    result = {}
    preguntas = Pregunta.query.all()
    result = preguntas_schema.dump(preguntas)
    
    data = {
        'message': 'Lista generada con éxito',
        'status': 200,
        'preguntas': result
    }

    return make_response(jsonify(data), 200)

@preguntas.route('/preguntas/get/<int:id_tipo_test>', methods=['GET'])
@jwt_required()
def get_preguntas_test(id_tipo_test):
    result = {}
    preguntas = Pregunta.query.filter_by(id_tipo_test=id_tipo_test).all()
    result = preguntas_schema.dump(preguntas)
    
    data = {
        'message': 'Lista generada con éxito',
        'status': 200,
        'preguntas': result
    }

    return make_response(jsonify(data), 200)

@preguntas.route('/preguntas/insert', methods=['POST'])
@jwt_required()
def insert():
    data = request.get_json()
    
    id_tipo_test = data.get('id_tipo_test')
    contenido = data.get('contenido')
    
    if id_tipo_test == None or contenido == None:
        data = {
            'message': 'Faltan datos',
            'status': 400
        }
        
        return make_response(jsonify(data), 400)
    
    pregunta = Pregunta(id_tipo_test, contenido)
    db.session.add(pregunta)
    db.session.commit()
    
    data = {
        'message': 'Pregunta creada con éxito',
        'status': 201,
        'pregunta': pregunta_schema.dump(pregunta)
    }
    
    return make_response(jsonify(data), 201)

@preguntas.route('/preguntas/update/<int:id_pregunta>', methods=['PUT'])
@jwt_required()
def update(id_pregunta):
    pregunta = Pregunta.query.get(id_pregunta)
    
    if not pregunta:
        data = {
            'message': 'No se encontró la pregunta',
            'status': 404
        }
        
        return make_response(jsonify(data), 404)
    
    pregunta.id_tipo_test = request.get_json().get('id_tipo_test')
    pregunta.contenido = request.get_json().get('contenido')
    
    db.session.commit()
    
    data = {
        'message': 'Pregunta actualizada con éxito',
        'status': 200,
        'pregunta': pregunta_schema.dump(pregunta)
    }
    
    return make_response(jsonify(data), 200)

@preguntas.route('/preguntas/delete/<int:id_pregunta>', methods=['DELETE'])
@jwt_required()
def delete(id_pregunta):
    pregunta = Pregunta.query.get(id_pregunta)
    
    if not pregunta:
        data = {
            'message': 'No se encontró la pregunta',
            'status': 404
        }
        
        return make_response(jsonify(data), 404)
    
    db.session.delete(pregunta)
    db.session.commit()
    
    data = {
        'message': 'Pregunta eliminada con éxito',
        'status': 200,
    }
    
    return make_response(jsonify(data), 200)