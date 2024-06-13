from flask import Blueprint, request, jsonify, make_response
from models.alternativa import Alternativa
from utils.db import db
from schemas.alternativa_schema import alternativa_schema, alternativas_schema
from flask_jwt_extended import jwt_required

alternativas = Blueprint('alternativas', __name__)

@alternativas.route('/alternativas/get', methods=['GET'])
@jwt_required()
def get_alternativas():
    alternativas = Alternativa.query.all()
    result = alternativas_schema.dump(alternativas)
    
    data = {
        'message': 'Lista generada con éxito',
        'status': 200,
        'alternativas': result
    }

    return make_response(jsonify(data), 200)

@alternativas.route('/alternativas/insert', methods=['POST'])
@jwt_required()
def insert():
    data = request.get_json()
    id_tipo_test = data.get('id_tipo_test')
    texto = data.get('texto')
    puntaje = data.get('puntaje')
    
    if not id_tipo_test or not texto or puntaje==None:
        data = {
            'message': 'Faltan datos',
            'status': 400
        }
        
        return make_response(jsonify(data), 400)
    
    alternativa = Alternativa(id_tipo_test, texto, puntaje)
    db.session.add(alternativa)
    db.session.commit()
    
    result = alternativa_schema.dump(alternativa)
    
    data = {
        'message': 'Alternativa creada con éxito',
        'status': 201,
        'data': result
    }
    
    return make_response(jsonify(result), 201)

@alternativas.route('/alternativas/update/<int:id>', methods=['PUT'])
@jwt_required()
def update(id):
    data = request.get_json()
    alternativa = Alternativa.query.get(id)
    
    if alternativa:
        alternativa.id_tipo_test = data.get('id_tipo_test')
        alternativa.texto = data.get('texto')
        alternativa.puntaje = data.get('puntaje')
        db.session.commit()
        
        result = alternativa_schema.dump(alternativa)
        
        data = {
            'message': 'Alternativa actualizada con éxito',
            'status': 200,
            'data': result
        }
        
        return make_response(jsonify(data), 200)
    
    data = {
        'message': 'Alternativa no encontrada',
        'status': 404
    }
    
    return make_response(jsonify(data), 404)

@alternativas.route('/alternativas/delete/<int:id>', methods=['DELETE'])
@jwt_required()
def delete(id):
    alternativa = Alternativa.query.get(id)
    
    if alternativa:
        db.session.delete(alternativa)
        db.session.commit()
        
        data = {
            'message': 'Alternativa eliminada con éxito',
            'status': 200
        }
        
        return make_response(jsonify(data), 200)
    
    data = {
        'message': 'Alternativa no encontrada',
        'status': 404
    }
    
    return make_response(jsonify(data), 404)