from flask import Blueprint, request, jsonify, make_response
from models.cita import Cita
from utils.db import db
from schemas.cita_schema import cita_schema, citas_schema
from flask_jwt_extended import jwt_required

citas = Blueprint('citas', __name__)

@citas.route('/citas/get', methods=['GET'])
@jwt_required()
def get_citas():
    result = {}
    citas = Cita.query.all()
    result = citas_schema.dump(citas)
    
    data = {
        'message': 'Lista generada con exito',
        'status': 200,
        'citas': result
    }
    
    return make_response(jsonify(data), 200)

@citas.route('/citas/insert', methods=['POST'])
@jwt_required()
def insert():
    data = request.get_json()
    
    id_paciente = data.get('id_paciente')
    id_especialista = data.get('id_especialista')
    motivo = data.get('motivo')
    detalle = data.get('detalle')
    estado = data.get('estado')
    
    if not estado:
        estado = 'En espera'

    cita = Cita(id_paciente, id_especialista, motivo, detalle, estado)

    db.session.add(cita)
    db.session.commit()
    
    data = {
        'message': 'Cita creada con exito',
        'status': 201,
        'cita': cita_schema.dump(cita)
    }
    
    return make_response(jsonify(data), 201)

#LA FUNCIÓN UPDATE NO SERÁ IMPLEMENTADA EN EL FRONTEND
@citas.route('/citas/update/<int:id_cita>', methods=['PUT'])
@jwt_required()
def update(id_cita):
    cita = Cita.query.get(id_cita)
    
    if cita==None:
        data = {
            'message': 'Cita no encontrada',
            'status': 400
        }
        
        return make_response(jsonify(data), 400)
    
    cita.id_paciente = request.get_json().get('id_paciente')
    cita.id_especialista = request.get_json().get('id_especialista')
    cita.motivo = request.get_json().get('motivo')
    cita.detalle = request.get_json().get('detalle')
    cita.estado = request.get_json().get('estado')
    
    db.session.commit()
    
    data = {
        'message': 'Cita actualizada con exito',
        'status': 200,
        'cita': cita_schema.dump(cita)
    }
    
    return make_response(jsonify(data), 200)

@citas.route('/citas/delete/<int:id_cita>', methods=['DELETE'])
@jwt_required()
def delete(id_cita):
    cita = Cita.query.get(id_cita)
    
    if not cita:
        data = {
            'message': 'Cita no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    
    db.session.delete(cita)
    db.session.commit()
    
    data = {
        'message': 'Cita eliminada con exito',
        'status': 200,
        'cita': cita_schema.dump(cita)
    }
    
    return make_response(jsonify(data), 200)