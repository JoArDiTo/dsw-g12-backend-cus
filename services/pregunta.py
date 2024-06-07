from flask import Blueprint, request, jsonify, make_response
from models.pregunta import Pregunta
from utils.db import db
from schemas.pregunta_schema import pregunta_schema, preguntas_schema
from flask_jwt_extended import jwt_required

preguntas = Blueprint('preguntas', __name__)

@preguntas.route('/preguntas/get', methods=['GET'])
@jwt_required()
def get_preguntas():
    preguntas = Pregunta.query.all()
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
    descripcion = data.get('descripcion')
    
    if not id_tipo_test or not descripcion:
        data = {
            'message': 'Faltan datos',
            'status': 400
        }
        
        return make_response(jsonify(data), 400)
    
    pregunta = Pregunta(id_tipo_test, descripcion)
    db.session.add(pregunta)
    db.session.commit()
    
    result = pregunta_schema.dump(pregunta)
    
    data = {
        'message': 'Pregunta creada con éxito',
        'status': 201,
        'data': result
    }
    
    return make_response(jsonify(result))

@preguntas.route('/preguntas/update/<int:id>', methods=['PUT'])
@jwt_required()
def update(id):
    data = request.get_json()
    pregunta = Pregunta.query.get(id)
    
    if pregunta:
        pregunta.id_tipo_test = data.get('id_tipo_test')
        pregunta.descripcion = data.get('descripcion')
        db.session.commit()
        
        result = pregunta_schema.dump(pregunta)
        
        data = {
            'message': 'Pregunta actualizada con éxito',
            'status': 200,
            'data': result
        }
        
        return make_response(jsonify(data), 200)
        
    data = {
        'message': 'No se encontró la pregunta',
        'status': 404
    }
    
    return make_response(jsonify(data), 404)

@preguntas.route('/preguntas/delete/<int:id>', methods=['DELETE'])
@jwt_required()
def delete(id):
    pregunta = Pregunta.query.get(id)
    
    if pregunta:
        db.session.delete(pregunta)
        db.session.commit()
        
        data = {
            'message': 'Pregunta eliminada con éxito',
            'status': 200
        }
        
        return make_response(jsonify(data), 200)
        
    data = {
        'message': 'No se encontró la pregunta',
        'status': 404
    }
    
    return make_response(jsonify(data), 404)