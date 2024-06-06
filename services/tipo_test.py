from flask import Blueprint, request, jsonify, make_response
from models.tipo_test import TipoTest
from utils.db import db
from schemas.tipo_test_schema import tipo_test_schema, tipos_test_schema

tipos_test = Blueprint('tipos_test', __name__)

@tipos_test.route('/tipos/get', methods=['GET'])
def get_tipos_test():
    tipos_test = TipoTest.query.all()
    result = tipos_test_schema.dump(tipos_test)
    
    data = {
        'message': 'Lista generada con éxito',
        'status': 200,
        'tipos_test': result
    }

    return make_response(jsonify(data), 200)

@tipos_test.route('/tipos/insert', methods=['POST'])
def insert():
    data = request.get_json()
    nombre = data.get('nombre')
    descripcion = data.get('descripcion')
    
    if not nombre:
        data = {
            'message': 'Faltan datos',
            'status': 400
        }
        
        return make_response(jsonify(data), 400)
    
    tipo_test = TipoTest(nombre, descripcion)
    db.session.add(tipo_test)
    db.session.commit()
    
    result = tipo_test_schema.dump(tipo_test)
    
    data = {
        'message': 'Tipo de test creado con éxito',
        'status': 201,
        'data': result
    }
    
    return make_response(jsonify(result))

@tipos_test.route('/tipos/update/<int:id>', methods=['PUT'])
def update(id):
    data = request.get_json()
    tipo_test = TipoTest.query.get(id)
    
    if tipo_test:
        tipo_test.nombre = data.get('nombre')
        tipo_test.descripcion = data.get('descripcion')
        db.session.commit()
        
        result = tipo_test_schema.dump(tipo_test)
        
        data = {
            'message': 'Tipo de test actualizado con éxito',
            'status': 200,
            'data': result
        }
        
        return make_response(jsonify(data), 200)
    
    data = {
        'message': 'No se encontró el tipo de test',
        'status': 404
    }
    
    return make_response(jsonify(data), 404)
        

@tipos_test.route('/tipos/delete/<int:id>', methods=['DELETE'])
def delete(id):
    tipo_test = TipoTest.query.get(id)
    
    if tipo_test:
        db.session.delete(tipo_test)
        db.session.commit()
        
        data = {
            'message': 'Tipo de test eliminado con éxito',
            'status': 200
        }
        
        return make_response(jsonify(data), 200)
    
    data = {
        'message': 'No se encontró el tipo de test',
        'status': 404
    }
    
    return make_response(jsonify(data), 404)