from flask import Blueprint, request, jsonify, make_response
from models.especialista import Especialista
from utils.db import db
from schemas.especialista_schema import especialista_schema, especialistas_schema
from flask_jwt_extended import jwt_required

especialistas = Blueprint('especialistas', __name__)

@especialistas.route('/especialistas/get', methods=['GET'])
@jwt_required()
def get_especialistas():
    result = {}
    especialistas = Especialista.query.all()
    result = especialistas_schema.dump(especialistas)
    
    data = {
        'message': 'Lista generada con exito',
        'status': 200,
        'especialistas': result
    }
    
    return make_response(jsonify(data), 200)

@especialistas.route('/especialistas/insert', methods=['POST'])
# NO SE REQUIERE JWT PARA CREAR ESPECIALISTA
def insert():
    data = request.get_json()
    
    id_usuario = data.get('id_usuario')
    licencia = data.get('licencia')
    especialidad = data.get('especialidad')
    
    especialista = Especialista(id_usuario, licencia, especialidad)
    db.session.add(especialista)
    db.session.commit()
    
    data = {
        'message': 'Especialista creado con exito',
        'status': 201,
        'especialista': especialista_schema.dump(especialista)
    }
    
    return make_response(jsonify(data), 201)

#LA FUNCIÓN UPDATE NO SERÁ IMPLEMENTADA EN EL FRONTEND
@especialistas.route('/especialistas/update/<int:id_especialista>', methods=['PUT'])
@jwt_required()
def update(id_especialista):
    especialista = Especialista.query.get(id_especialista)
    
    if especialista==None:
        data = {
            'message': 'Especialista no encontrado',
            'status': 400
        }
        
        return make_response(jsonify(data), 400)
    
    especialista.id_usuario = request.get_json().get('id_usuario')
    especialista.licencia = request.get_json().get('licencia')
    especialista.especialidad = request.get_json().get('especialidad')
    
    db.session.commit()
    
    data = {
        'message': 'Especialista actualizado con exito',
        'status': 200,
        'especialista': especialista_schema.dump(especialista)
    }
    
    return make_response(jsonify(data), 200)

@especialistas.route('/especialistas/delete/<int:id_especialista>', methods=['DELETE'])
@jwt_required()
def delete(id_especialista):
    especialista = Especialista.query.get(id_especialista)
    
    if not especialista:
        data = {
            'message': 'Especialista no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    
    db.session.delete(especialista)
    db.session.commit()
    
    data = {
        'message': 'Especialista eliminado con exito',
        'status': 200,
        'especialista': especialista_schema.dump(especialista)
    }
    
    return make_response(jsonify(data), 200)