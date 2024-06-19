from flask import Blueprint, request, jsonify, make_response
from models.tratamiento import Tratamiento
from utils.db import db
from schemas.tratamiento_schema import tratamiento_schema, tratamientos_schema
from flask_jwt_extended import jwt_required

tratamientos = Blueprint('tratamientos', __name__)

@tratamientos.route('/tratamientos/get', methods=['GET'])
@jwt_required()
def get_tratamientos():
    result = {}
    tratamientos = Tratamiento.query.all()
    result = tratamientos_schema.dump(tratamientos)
    
    data = {
        'message': 'Lista generada con exito',
        'status': 200,
        'tratamientos': result
    }
    
    return make_response(jsonify(data), 200)

@tratamientos.route('/tratamientos/insert', methods=['POST'])
@jwt_required()
def insert():
    data = request.get_json()
    
    descripcion = data.get('descripcion')
    fecha = data.get('fecha')
    
    tratamiento = Tratamiento(descripcion, fecha)
    db.session.add(tratamiento)
    db.session.commit()
    
    data = {
        'message': 'Tratamiento creado con exito',
        'status': 201,
        'tratamiento': tratamiento_schema.dump(tratamiento)
    }
    
    return make_response(jsonify(data), 201)

#LA FUNCIÓN UPDATE NO SERÁ IMPLEMENTADA EN EL FRONTEND
@tratamientos.route('/tratamientos/update/<int:id_tratamiento>', methods=['PUT'])
@jwt_required()
def update(id_tratamiento):
    tratamiento = Tratamiento.query.get(id_tratamiento)
    
    if tratamiento==None:
        data = {
            'message': 'Tratamiento no encontrado',
            'status': 400
        }
        
        return make_response(jsonify(data), 400)
    
    tratamiento.descripcion = request.get_json().get('descripcion')
    tratamiento.fecha = request.get_json().get('fecha')
    db.session.commit()
    
    data = {
        'message': 'Tratamiento actualizado con exito',
        'status': 200,
        'tratamiento': tratamiento_schema.dump(tratamiento)
    }
    
    return make_response(jsonify(data), 200)

@tratamientos.route('/tratamientos/delete/<int:id_tratamiento>', methods=['DELETE'])
@jwt_required()
def delete(id_tratamiento):
    tratamiento = Tratamiento.query.get(id_tratamiento)
    
    if tratamiento==None:
        data = {
            'message': 'Tratamiento no encontrado',
            'status': 400
        }
        
        return make_response(jsonify(data), 400)
    
    db.session.delete(tratamiento)
    db.session.commit()
    
    data = {
        'message': 'Tratamiento eliminado con exito',
        'status': 200,
        'tratamiento': tratamiento_schema.dump(tratamiento)
    }
    
    return make_response(jsonify(data), 200)