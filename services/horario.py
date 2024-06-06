from flask import Blueprint, request, jsonify, make_response
from models.horario import Horario
from utils.db import db
from schemas.horario_schema import horario_schema, horarios_schema

horarios = Blueprint('horarios', __name__)

@horarios.route('/horarios/get', methods=['GET'])
def get_horarios():
    horarios = Horario.query.all()
    result = horarios_schema.dump(horarios)
    
    data = {
        'message': 'Lista generada con éxito',
        'status': 200,
        'horarios': result
    }

    return make_response(jsonify(data), 200)

@horarios.route('/horarios/insert', methods=['POST'])
def insert():
    data = request.get_json()
    id_especialista = data.get('id_especialista')
    estado = data.get('estado')
    
    if not id_especialista or not estado:
        data = {
            'message': 'Faltan datos',
            'status': 400
        }
        
        return make_response(jsonify(data), 400)
    
    horario = Horario(id_especialista, estado)
    db.session.add(horario)
    db.session.commit()
    
    result = horario_schema.dump(horario)
    
    data = {
        'message': 'Horario creado con éxito',
        'status': 201,
        'data': result
    }
    
    return make_response(jsonify(data), 201)

@horarios.route('/horarios/update/<int:id>', methods=['PUT'])
def update(id):
    horario = Horario.query.get(id)
    
    if horario:
        horario.id_especialista = request.json.get('id_especialista')
        horario.estado = request.json.get('estado')
        
        db.session.commit()
        
        result = horario_schema.dump(horario)
        
        data = {
            'message': 'Horario actualizado con éxito',
            'status': 200,
            'data': result
        }
        
        return make_response(jsonify(data), 200)
    
    data = {
        'message': 'Horario no encontrado',
        'status': 404
    }
    
    return make_response(jsonify(data), 404)

@horarios.route('/horarios/delete/<int:id>', methods=['DELETE'])
def delete(id):
    result = {}
    horario = Horario.query.get(id)
    
    if horario:
        db.session.delete(horario)
        db.session.commit()
        
        result = horario_schema.dump(horario)
        
        data = {
            'message': 'Horario eliminado con éxito',
            'status': 200,
            'data': result
        }
        
        return make_response(jsonify(data), 200)
    
    data = {
        'message': 'Horario no encontrado',
        'status': 404
    }
    
    return make_response(jsonify(data), 404)