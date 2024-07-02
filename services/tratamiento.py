from schemas.tratamiento_schema import tratamiento_schema, tratamientos_schema
from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import jwt_required
from models.tratamiento import Tratamiento
from utils.db import db

tratamientos = Blueprint('tratamientos', __name__)

@tratamientos.route('/tratamientos/get', methods=['GET'])
@jwt_required()
def get_tratamientos():
    result = {}
    tratamientos = Tratamiento.query.all()
    result = tratamientos_schema.dump(tratamientos)
    
    data = {
        'message': 'Lista generada con éxito',
        'status': 200,
        'tratamientos': result
    }

    return make_response(jsonify(data), 200)

@tratamientos.route('/tratamientos/get/<int:id_tratamiento>', methods=['GET'])
@jwt_required()
def get_tratamiento(id_tratamiento):
    tratamiento = Tratamiento.query.get(id_tratamiento)
    
    if not tratamiento:
        data = {
            'message': 'No se encontró el tratamiento',
            'status': 404
        }
        
        return make_response(jsonify(data), 404)
    
    data = {
        'message': 'Tratamiento encontrado con éxito',
        'status': 200,
        'tratamiento': tratamiento_schema.dump(tratamiento)
    }
    
    return make_response(jsonify(data), 200)

@tratamientos.route('/tratamientos/insert', methods=['POST'])
@jwt_required()
def insert():
    data = request.get_json()
    
    descripcion = data.get('descripcion')
    fundamentacion = data.get('fundamentacion')
    
    if descripcion==None or fundamentacion==None:
        data = {
            'message': 'Faltan datos',
            'status': 400
        }
        
        return make_response(jsonify(data), 400)
    
    tratamiento = Tratamiento(descripcion, fundamentacion)
    db.session.add(tratamiento)
    db.session.commit()
    
    data = {
        'message': 'Tratamiento creado con éxito',
        'status': 201,
        'tratamiento': tratamiento_schema.dump(tratamiento)
    }
    
    return make_response(jsonify(data), 201)

@tratamientos.route('/tratamientos/update/<int:id_tratamiento>', methods=['PUT'])
@jwt_required()
def update(id_tratamiento):
    tratamiento = Tratamiento.query.get(id_tratamiento)
    
    if not tratamiento:
        data = {
            'message': 'No se encontró el tratamiento',
            'status': 404
        }
        
        return make_response(jsonify(data), 404)
    
    tratamiento.descripcion = request.json['descripcion']
    tratamiento.fundamentacion = request.json['fundamentacion']
    
    db.session.commit()
    
    data = {
        'message': 'Tratamiento actualizado con éxito',
        'status': 200,
        'tratamiento': tratamiento_schema.dump(tratamiento)
    }
    
    return make_response(jsonify(data), 200)
  
@tratamientos.route('/tratamientos/delete/<int:id_tratamiento>', methods=['DELETE'])
@jwt_required()
def delete(id_tratamiento):
    tratamiento = Tratamiento.query.get(id_tratamiento)
    
    if not tratamiento:
        data = {
            'message': 'No se encontró el tratamiento',
            'status': 404
        }
        
        return make_response(jsonify(data), 404)
    
    db.session.delete(tratamiento)
    db.session.commit()
    
    data = {
        'message': 'Tratamiento eliminado con éxito',
        'status': 200
    }
    
    return make_response(jsonify(data), 200)