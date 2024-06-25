from flask import Blueprint, request, jsonify, make_response
from models.semaforo import Semaforo
from utils.db import db
from schemas.semaforo_schema import semaforo_schema, semaforos_schema
from flask_jwt_extended import jwt_required

semaforos = Blueprint('semaforos', __name__)

@semaforos.route('/semaforos/get', methods=['GET'])
@jwt_required()
def get_semaforos():
    result = {}
    semaforos = Semaforo.query.all()
    result = semaforos_schema.dump(semaforos)
    
    data = {
        'message': 'Lista generada con éxito',
        'status': 200,
        'semaforos': result
    }
    
    return make_response(jsonify(data),200)

@semaforos.route('/semaforos/insert', methods=['POST'])
def insert_semaforo():
    data = request.get_json()
    
    color = data['color']
    
    if color == None:
        data = {
            'message': 'Faltan datos',
            'status': 400
        }
        
        return make_response(jsonify(data),400)
    
    semaforo = Semaforo(color)
    db.session.add(semaforo)
    db.session.commit()
    
    data = {
        'message': 'Semaforo creado con éxito',
        'status': 201,
        'semaforo': semaforo_schema.dump(semaforo)
    }
    
    return make_response(jsonify(data),201)

@semaforos.route('/semaforos/update/<int:id_semaforo>', methods=['PUT'])
@jwt_required()
def update_semaforo(id_semaforo):
    semaforo = Semaforo.query.get(id_semaforo)
    
    if not semaforo:
        data = {
            'message': 'No se encontró el semaforo',
            'status': 404
        }
        
        return make_response(jsonify(data),404)
    
    data = request.get_json()
    
    semaforo.color = data.get('color', semaforo.color)
    
    db.session.commit()
    
    data = {
        'message': 'Semaforo actualizado con éxito',
        'status': 200,
        'semaforo': semaforo_schema.dump(semaforo)
    }
    
    return make_response(jsonify(data),200)

@semaforos.route('/semaforos/delete/<int:id_semaforo>', methods=['DELETE'])
@jwt_required()
def delete_semaforo(id_semaforo):
    semaforo = Semaforo.query.get(id_semaforo)
    
    if not semaforo:
        data = {
            'message': 'No se encontró el semaforo',
            'status': 404
        }
        
        return make_response(jsonify(data),404)
    
    db.session.delete(semaforo)
    db.session.commit()
    
    data = {
        'message': 'Semaforo eliminado con éxito',
        'status': 200
    }
    
    return make_response(jsonify(data),200)