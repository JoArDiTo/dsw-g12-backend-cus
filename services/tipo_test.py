from flask import Blueprint, request, jsonify, make_response
from models.tipo_test import TipoTest
from utils.db import db
from schemas.tipo_test_schema import tipo_test_schema, tipos_test_schema
from flask_jwt_extended import jwt_required

tipos_test = Blueprint('tipos_test', __name__)

@tipos_test.route('/tipos/get', methods=['GET'])
@jwt_required()
def get_tipos_test():
    result = {}
    tipos_test = TipoTest.query.all()
    result = tipos_test_schema.dump(tipos_test)
    
    data = {
        'message': 'Lista generada con éxito',
        'status': 200,
        'tipos_test': result
    }

    return make_response(jsonify(data), 200)

@tipos_test.route('/tipos/insert', methods=['POST'])
@jwt_required()
def insert():
    data = request.get_json()
    
    nombre = data.get('nombre')
    autor = data.get('autor')
    descripcion = data.get('descripcion')
    
    if nombre == None or autor == None or descripcion == None:
        data = {
            'message': 'Faltan datos',
            'status': 400
        }
        
        return make_response(jsonify(data), 400)
    
    tipo_test = TipoTest(nombre, autor, descripcion)
    db.session.add(tipo_test)
    db.session.commit()
    
    data = {
        'message': 'Tipo de test creado con éxito',
        'status': 201,
        'tipo_test': tipo_test_schema.dump(tipo_test)
    }
    
    return make_response(jsonify(data), 201)

@tipos_test.route('/tipos/update/<int:id_tipo_test>', methods=['PUT'])
@jwt_required()
def update(id_tipo_test):
    tipo_test = TipoTest.query.get(id_tipo_test)
    
    if not tipo_test:
        data = {
            'message': 'Tipo de test no encontrado',
            'status': 400
        }
        
        return make_response(jsonify(data), 400)
    
    tipo_test.nombre = request.get_json().get('nombre')
    tipo_test.autor = request.get_json().get('autor')
    tipo_test.descripcion = request.get_json().get('descripcion')
    
    db.session.commit()
    
    data = {
        'message': 'Tipo de test actualizado con éxito',
        'status': 200,
        'tipo_test': tipo_test_schema.dump(tipo_test)
    }
    
    return make_response(jsonify(data), 200)

@tipos_test.route('/tipos/delete/<int:id_tipo_test>', methods=['DELETE'])
@jwt_required()
def delete(id_tipo_test):
    tipo_test = TipoTest.query.get(id_tipo_test)
    
    if not tipo_test:
        data = {
            'message': 'Tipo de test no encontrado',
            'status': 400
        }
        
        return make_response(jsonify(data), 400)
    
    db.session.delete(tipo_test)
    db.session.commit()
    
    data = {
        'message': 'Tipo de test eliminado con éxito',
        'status': 200
    }
    
    return make_response(jsonify(data), 200)