from schemas.ansiedad_schema import ansiedad_schema, ansiedades_schema
from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import jwt_required
from models.ansiedad import Ansiedad
from utils.db import db

ansiedades = Blueprint('ansiedades', __name__)

@ansiedades.route('/ansiedades/get', methods=['GET'])
@jwt_required()
def get_ansiedades():
    result = {}
    ansiedades = Ansiedad.query.all()
    result = ansiedades_schema.dump(ansiedades)
    
    data = {
        'message': 'Lista generada con éxito',
        'status': 200,
        'ansiedades': result
    }

    return make_response(jsonify(data), 200)
  
@ansiedades.route('/ansiedades/insert', methods=['POST'])
@jwt_required()
def insert():
    data = request.get_json()
    
    id_especialista = data.get('id_especialista')
    contenido = data.get('contenido')
    
    if id_especialista==None or contenido==None:
        data = {
            'message': 'Faltan datos',
            'status': 400
        }
        
        return make_response(jsonify(data), 400)
    
    ansiedad = Ansiedad(id_especialista, contenido)
    db.session.add(ansiedad)
    db.session.commit()
    
    data = {
        'message': 'Ansiedad creada con éxito',
        'status': 201,
        'ansiedad': ansiedad_schema.dump(ansiedad)
    }
    
    return make_response(jsonify(data), 201)

@ansiedades.route('/ansiedades/update/<int:id_ansiedad>', methods=['PUT'])
@jwt_required()
def update(id_ansiedad):
    ansiedad = Ansiedad.query.get(id_ansiedad)
    
    if not ansiedad:
        data = {
            'message': 'No se encontró la ansiedad',
            'status': 404
        }
        
        return make_response(jsonify(data), 404)
    
    ansiedad.id_especialista = request.json['id_especialista']
    ansiedad.contenido = request.json['contenido']
    db.session.commit()
    
    data = {
        'message': 'Ansiedad actualizada con éxito',
        'status': 200,
        'ansiedad': ansiedad_schema.dump(ansiedad)
    }
    
    return make_response(jsonify(data), 200)
  
@ansiedades.route('/ansiedades/delete/<int:id_ansiedad>', methods=['DELETE'])
@jwt_required()
def delete(id_ansiedad):
    ansiedad = Ansiedad.query.get(id_ansiedad)
    
    if not ansiedad:
        data = {
            'message': 'No se encontró la ansiedad',
            'status': 404
        }
        
        return make_response(jsonify(data), 404)
    
    db.session.delete(ansiedad)
    db.session.commit()
    
    data = {
        'message': 'Ansiedad eliminada con éxito',
        'status': 200
    }
    
    return make_response(jsonify(data), 200)