from flask import Blueprint, request, jsonify, make_response
from models.especialista import Especialista
from models.usuario import Usuario
from utils.db import db
from schemas.especialista_schema import especialista_schema, especialistas_schema
from flask_jwt_extended import jwt_required

especialistas = Blueprint('especialistas', __name__)

@especialistas.route('/especialistas/get', methods=['GET'])
@jwt_required()
def get_especialistas():
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
    numero_de_colegiatura = request.json.get('numero_de_colegiatura')
    documento = request.json.get('documento')
    
    if Especialista.query.filter_by(numero_de_colegiatura=numero_de_colegiatura).first():
        # En caso no se cree el especialista para el usuario, borramos dicho usuario
        usuario = Usuario.query.get(documento)
        db.session.delete(usuario)
        db.session.commit()
        data = {
            'message': 'Número de colegiatura ya registrado',
            'status': 400
        }
        
        return make_response(jsonify(data), 400)
    
    if not numero_de_colegiatura or not documento:
        data = {
            'message': 'Faltan datos',
            'status': 400
        }
        
        return make_response(jsonify(data), 400)
    
    new_especialista = Especialista(numero_de_colegiatura, documento)
    
    db.session.add(new_especialista)
    db.session.commit()
    
    result = especialista_schema.dump(new_especialista)
    
    data = {
        'message': 'Especialista creado con exito',
        'status': 201,
        'especialista': result
    }
    
    return make_response(jsonify(data), 201)

#LA FUNCIÓN UPDATE NO SERÁ IMPLEMENTADA EN EL FRONTEND
@especialistas.route('/especialistas/update/<int:id_especialista>', methods=['PUT'])
@jwt_required()
def update(id_especialista):
    especialista = Especialista.query.get(id_especialista)
    
    if especialista:
        especialista.numero_de_colegiatura = request.json.get('numero_de_colegiatura')
        especialista.documento = request.json.get('documento')
        
        db.session.commit()
        
        result = especialista_schema.dump(especialista)
        
        data = {
            'message': 'Especialista actualizado con exito',
            'status': 200,
            'especialista': result
        }
        
        return make_response(jsonify(data), 200)
    
    data = {
        'message': 'Especialista no encontrado',
        'status': 404
    }
    
    return make_response(jsonify(data), 404)

@especialistas.route('/especialistas/delete/<int:id_especialista>', methods=['DELETE'])
@jwt_required()
def delete(id_especialista):
    especialista = Especialista.query.get(id_especialista)
    
    if especialista:
        db.session.delete(especialista)
        db.session.commit()
        
        data = {
            'message': 'Especialista eliminado con exito',
            'status': 200
        }
        
        return make_response(jsonify(data), 200)
    
    data = {
        'message': 'Especialista no encontrado',
        'status': 404
    }
    
    return make_response(jsonify(data), 404)