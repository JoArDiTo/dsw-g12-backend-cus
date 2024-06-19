from flask import Blueprint, request, jsonify, make_response
from models.diagnostico import Diagnostico
from utils.db import db
from schemas.diagnostico_schema import diagnostico_schema, diagnosticos_schema
from flask_jwt_extended import jwt_required

diagnosticos = Blueprint('diagnosticos', __name__)

@diagnosticos.route('/diagnosticos/get', methods=['GET'])
@jwt_required()
def get_diagnosticos():
    result = {}
    diagnosticos = Diagnostico.query.all()
    result = diagnosticos_schema.dump(diagnosticos)
    
    data = {
        'message': 'Lista generada con exito',
        'status': 200,
        'diagnosticos': result
    }
    
    return make_response(jsonify(data), 200)

@diagnosticos.route('/diagnosticos/insert', methods=['POST'])
@jwt_required()
def insert():
    data = request.get_json()
    
    id_paciente = data.get('id_paciente')
    id_especialista = data.get('id_especialista')
    id_tratamiento = data.get('id_tratamiento')
    
    if id_paciente == None or id_especialista == None or id_tratamiento == None:
        data = {
            'message': 'Faltan datos',
            'status': 400
        }
        
        return make_response(jsonify(data), 400)
    
    diagnostico = Diagnostico(id_paciente, id_especialista, id_tratamiento)
    db.session.add(diagnostico)
    db.session.commit()
    
    data = {
        'message': 'Diagnostico creado con exito',
        'status': 201,
        'diagnostico': diagnostico_schema.dump(diagnostico)
    }
    
    return make_response(jsonify(data), 201)

#LA FUNCIÓN UPDATE NO SERÁ IMPLEMENTADA EN EL FRONTEND
@diagnosticos.route('/diagnosticos/update/<int:id_diagnostico>', methods=['PUT'])
@jwt_required()
def update(id_diagnostico):
    diagnostico = Diagnostico.query.get(id_diagnostico)
    
    if diagnostico==None:
        data = {
            'message': 'Diagnostico no encontrado',
            'status': 400
        }
        
        return make_response(jsonify(data), 400)
    
    diagnosticos.id_paciente = request.get_json().get('id_paciente')
    diagnosticos.id_especialista = request.get_json().get('id_especialista')
    diagnosticos.id_tratamiento = request.get_json().get('id_tratamiento')
    
    db.session.commit()
    
    data = {
        'message': 'Diagnostico actualizado con exito',
        'status': 200,
        'diagnostico': diagnostico_schema.dump(diagnostico)
    }
    
    return make_response(jsonify(data), 200)

@diagnosticos.route('/diagnosticos/delete/<int:id_diagnostico>', methods=['DELETE'])
@jwt_required()
def delete(id_diagnostico):
    diagnostico = Diagnostico.query.get(id_diagnostico)
    
    if diagnostico==None:
        data = {
            'message': 'Diagnostico no encontrado',
            'status': 400
        }
        
        return make_response(jsonify(data), 400)
    
    db.session.delete(diagnostico)
    db.session.commit()
    
    data = {
        'message': 'Diagnostico eliminado con exito',
        'status': 200,
        'diagnostico': diagnostico_schema.dump(diagnostico)
    }
    
    return make_response(jsonify(data), 200)