from flask import Blueprint, request, jsonify, make_response
from models.persona import Persona
from utils.db import db
from schemas.persona_schema import persona_schema, personas_schema
from flask_jwt_extended import jwt_required

personas = Blueprint('personas', __name__)

@personas.route('/personas/get', methods=['GET'])
@jwt_required()
def get_personas():
    result = {}
    personas = Persona.query.all()
    result = personas_schema.dump(personas)
    
    data = {
        'message': 'Lista generada con éxito',
        'status': 200,
        'personas': result
    }
    
    return make_response(jsonify(data),200)

@personas.route('/personas/insert', methods=['POST'])
def insert_persona():
    data = request.get_json()
    
    documento = data['documento']
    tipo_documento = data['tipo_documento']
    nombre = data['nombre']
    apellido_paterno = data['apellido_paterno']
    apellido_materno = data['apellido_materno']
    telefono = data['telefono']
    fecha_nacimiento = data['fecha_nacimiento']
    sexo = data['sexo']
    id_ubigeo = data['id_ubigeo']
    
    if Persona.query.get(documento):
        data = {
            'message': 'Datos de persona ya registrada',
            'status': 400
        }
        
        return make_response(jsonify(data),400)
    
    if documento==None or tipo_documento==None or nombre==None or apellido_paterno==None or apellido_materno==None or telefono==None or fecha_nacimiento==None or sexo==None or id_ubigeo==None:
        data = {
            'message': 'Faltan datos',
            'status': 400
        }
        
        return make_response(jsonify(data),400)
    
    persona = Persona(documento,tipo_documento,nombre,apellido_paterno,apellido_materno,telefono,fecha_nacimiento,sexo,id_ubigeo)
    
    db.session.add(persona)
    db.session.commit()
    
    data = {
        'message': 'Persona creada con éxito',
        'status': 200,
        'persona': persona_schema.dump(persona)
    }
    
    return make_response(jsonify(data),200)

@personas.route('/personas/update/<string:documento>', methods=['PUT'])
def update_persona(documento):    
    persona = Persona.query.get(documento)
    
    if persona==None:
        data = {
            'message': 'Persona no encontrada',
            'status': 400
        }
        
        return make_response(jsonify(data),400)
    
    #persona.documento = request.json.get('documento')
    #persona.tipo_documento = request.json.get('tipo_documento')
    persona.nombre = request.json.get('nombre')
    persona.apellido_paterno = request.json.get('apellido_paterno')
    persona.apellido_materno = request.json.get('apellido_materno')
    persona.telefono = request.json.get('telefono')
    persona.fecha_nacimiento = request.json.get('fecha_nacimiento')
    persona.sexo = request.json.get('sexo')
    persona.id_ubigeo = request.json.get('id_ubigeo')
    
    db.session.commit()
    
    data = {
        'message': 'Persona actualizada con éxito',
        'status': 200,
        'persona': persona_schema.dump(persona)
    }
    
    return make_response(jsonify(data),200)

@personas.route('/personas/delete/<string:documento>', methods=['DELETE'])
def delete_persona(documento):
    persona = Persona.query.get(documento)
    
    if persona==None:
        data = {
            'message': 'Persona no encontrada',
            'status': 400
        }
        
        return make_response(jsonify(data),400)
    
    db.session.delete(persona)
    db.session.commit()
    
    data = {
        'message': 'Persona eliminada con éxito',
        'status': 200
    }
    
    return make_response(jsonify(data),200)