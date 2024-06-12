from flask import Blueprint, request, jsonify, make_response
from models.cita import Cita
from utils.db import db
from schemas.cita_schema import cita_schema, citas_schema
from flask_jwt_extended import jwt_required

citas = Blueprint('citas', __name__)

@citas.route('/citas/get', methods=['GET'])
@jwt_required()
def get_citas():
    citas = Cita.query.all()
    result = citas_schema.dump(citas)
    
    data = {
        'message': 'Lista generada con éxito',
        'status': 200,
        'citas': result
    }
    
    return make_response(jsonify(data), 200)

@citas.route('/citas/insert', methods=['POST'])
@jwt_required()
def insert():
    data = request.get_json()
    id_atencion = data.get('id_atencion')
    id_historial_clinico = data.get('id_historial_clinico')
    estado = data.get('estado')
    observaciones = data.get('observaciones')
    
    if not id_atencion or not id_historial_clinico or not estado: #Observaciones puede ser nulo
        data = {
            'message': 'Faltan datos',
            'status': 400
        }
        
        return make_response(jsonify(data), 400)
    
    new_cita = Cita(id_atencion, id_historial_clinico, estado, observaciones)
    
    db.session.add(new_cita)
    db.session.commit()
    
    result = cita_schema.dump(new_cita)
    
    data = {
        'message': 'Cita creada con éxito',
        'status': 201,
        'cita': result
    }
    
    return make_response(jsonify(data), 201)

@citas.route('/citas/update/<int:id_cita>', methods=['PUT'])
@jwt_required()
def update(id_cita):
    cita = Cita.query.get(id_cita)
    
    if cita:
        cita.id_atencion = request.json.get('id_atencion')
        cita.id_historial_clinico = request.json.get('id_historial_clinico')
        cita.estado = request.json.get('estado')
        if data.get('observaciones'):
            cita.observaciones = request.json.get('observaciones')
        
        db.session.commit()
        
        result = cita_schema.dump(cita)
        
        data = {
            'message': 'Cita actualizada con éxito',
            'status': 200,
            'cita': result
        }
        
        return make_response(jsonify(data), 200)
    
    data = {
        'message': 'Cita no encontrada',
        'status': 404
    }
    
    return make_response(jsonify(data), 404)

@citas.route('/citas/delete/<int:id_cita>', methods=['DELETE'])
@jwt_required()
def delete(id_cita):
    cita = Cita.query.get(id_cita)
    
    if cita:
        db.session.delete(cita)
        
        data = {
            'message': 'Cita eliminada con éxito',
            'status': 200
        }
        
        return make_response(jsonify(data), 200)
    
    data = {
        'message': 'Cita no encontrada',
        'status': 404
    }
    
    return make_response(jsonify(data), 404)