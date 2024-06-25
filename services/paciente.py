from flask import Blueprint, request, jsonify, make_response
from models.paciente import Paciente
from utils.db import db
from schemas.paciente_schema import paciente_schema, pacientes_schema
from flask_jwt_extended import jwt_required

pacientes = Blueprint('pacientes', __name__)

@pacientes.route('/pacientes/get', methods=['GET'])
@jwt_required()
def get_pacientes():
    result = {}
    pacientes = Paciente.query.all()
    result = pacientes_schema.dump(pacientes)
    
    data = {
        'message':'Lista generada con éxito',
        'status': 200,
        'pacientes': result
    }
    
    return make_response(jsonify(data),200)    

@pacientes.route('/pacientes/get/<int:id_usuario>', methods=['GET'])
def get_paciente(id_usuario):
    paciente = Paciente.query.filter_by(id_usuario=id_usuario).first()
    
    if paciente==None:
        data = {
            'message': 'Estudiante no encontrado',
            'status': 404
        }
        
        return make_response(jsonify(data),404)
    
    data = {
        'message': 'Estudiante encontrado con éxito',
        'status': 200,
        'paciente': paciente_schema.dump(paciente)
    }
    
    return make_response(jsonify(data),200)

@pacientes.route('/pacientes/insert', methods=['POST'])
def insert(): #NO SE REQUIERE JWT PARA CREAR PACIENTE
    data = request.get_json()
    
    id_usuario = data.get('id_usuario')
    
    paciente = Paciente(id_usuario)
    db.session.add(paciente)
    db.session.commit()
    
    data = {
        'message': 'Estudiante creado con éxito',
        'status': 201,
        'paciente': paciente_schema.dump(paciente)
    }
    
    return make_response(jsonify(data),201)

@pacientes.route('/pacientes/update/<int:id_paciente>', methods=['PUT'])
@jwt_required()
def update(id_paciente):
    paciente = Paciente.query.get(id_paciente)
    
    if not paciente:
        data = {
            'message': 'Estudiante no encontrado',
            'status': 400
        }
        
        return make_response(jsonify(data),400)
    
    paciente.id_usuario = request.get_json().get('id_usuario')
    
    db.session.commit()
    
    data = {
        'message': 'Estudiante actualizado con éxito',
        'status': 200,
        'paciente': paciente_schema.dump(paciente)
    }
    
    return make_response(jsonify(data),200)

@pacientes.route('/pacientes/delete/<int:id_paciente>', methods=['DELETE'])
@jwt_required()
def delete(id_paciente):
    paciente = Paciente.query.get(id_paciente)
    
    if not paciente:
        data = {
            'message': 'Estudiante no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    
    db.session.delete(paciente)
    db.session.commit()
    
    data = {
        'message': 'Estudiante eliminado con éxito',
        'status': 200,
    }
    
    return make_response(jsonify(data), 200)