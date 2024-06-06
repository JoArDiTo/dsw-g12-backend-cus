from flask import Blueprint, request, jsonify, make_response
from models.atencion import Atencion
from utils.db import db
from schemas.atencion_schema import atencion_schema, atenciones_schema

atenciones = Blueprint('atenciones', __name__)

@atenciones.route('/atenciones/get', methods=['GET'])
def get_atenciones():
    atenciones = Atencion.query.all()
    result = atenciones_schema.dump(atenciones)
    
    data = {
        'message': 'Lista generada con éxito',
        'status': 200,
        'atenciones': result
    }
    
    return make_response(jsonify(data), 200)

@atenciones.route('/atenciones/insert', methods=['POST'])
def insert():
    data = request.get_json()
    id_horario = data.get('id_horario')
    fecha = data.get('fecha')
    hora_inicio = data.get('hora_inicio')
    hora_fin = data.get('hora_fin')
    reservado = data.get('reservado')
    
    if not id_horario or not fecha or not hora_inicio or not hora_fin or not reservado:
        data = {
            'message': 'Faltan datos',
            'status': 400
        }
        
        return make_response(jsonify(data), 400)
    
    new_atencion = Atencion(id_horario, fecha, hora_inicio, hora_fin, reservado)
    
    db.session.add(new_atencion)
    db.session.commit()
    
    result = atencion_schema.dump(new_atencion)
    
    data = {
        'message': 'Atencion creada con éxito',
        'status': 201,
        'atencion': result
    }
    
    return make_response(jsonify(data), 201)

@atenciones.route('/atenciones/update/<int:id_atencion>', methods=['PUT'])
def update(id_atencion):
    atencion = Atencion.query.get(id_atencion)
    
    if atencion:
        atencion.id_horario = request.json.get('id_horario')
        atencion.fecha = request.json.get('fecha')
        atencion.hora_inicio = request.json.get('hora_inicio')
        atencion.hora_fin = request.json.get('hora_fin')
        atencion.reservado = request.json.get('reservado')
        
        db.session.commit()
        
        result = atencion_schema.dump(atencion)
        
        data = {
            'message': 'Atencion actualizada con éxito',
            'status': 200,
            'atencion': result
        }
        
        return make_response(jsonify(data), 200)
    
    data = {
        'message': 'Atencion no encontrada',
        'status': 404
    }
    
    return make_response(jsonify(data), 404)

@atenciones.route('/atenciones/delete/<int:id_atencion>', methods=['DELETE'])
def delete(id_atencion):
    atencion = Atencion.query.get(id_atencion)
    
    if atencion:
        db.session.delete(atencion)
        db.session.commit()
        
        result = atencion_schema.dump(atencion)
        
        data = {
            'message': 'Atencion eliminada con éxito',
            'status': 200,
            'atencion': result
        }
        
        return make_response(jsonify(data), 200)
    
    data = {
        'message': 'Atencion no encontrada',
        'status': 404
    }
    
    return make_response(jsonify(data), 404)
    
    