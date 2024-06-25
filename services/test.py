from flask import Blueprint, request, jsonify, make_response
from models.test import Test
from utils.db import db
from schemas.test_schema import test_schema, tests_schema
from flask_jwt_extended import jwt_required

tests = Blueprint('tests', __name__)

@tests.route('/tests/get', methods=['GET'])
@jwt_required()
def get_tests():
    result = {}
    tests = Test.query.all()
    result = tests_schema.dump(tests)
    
    data = {
        'message': 'Lista generada con éxito',
        'status': 200,
        'tests': result
    }

    return make_response(jsonify(data), 200)

@tests.route('/tests/insert', methods=['POST'])
@jwt_required()
def insert():
    data = request.get_json()
    
    id_tipo_test = data.get('id_tipo_test')
    id_paciente = data.get('id_paciente')
    resultado = data.get('resultado')
    interpretacion = data.get('interpretacion')
    color = data.get('color')
    fecha = data.get('fecha')
    
    if id_tipo_test==None or id_paciente==None or resultado==None or interpretacion==None or color==None or fecha==None:
        data = {
            'message': 'Faltan datos',
            'status': 400
        }
        
        return make_response(jsonify(data), 400)

    test = Test(id_tipo_test, id_paciente, resultado, interpretacion, color, fecha) 
    db.session.add(test)
    db.session.commit()
    
    data = {
        'message': 'Test creado con éxito',
        'status': 201,
        'test': test_schema.dump(test)
    }
    
    return make_response(jsonify(data), 201) 

@tests.route('/tests/update/<int:id_test>', methods=['PUT'])
@jwt_required()
def update(id_test):
    test = Test.query.get(id_test)
    
    if not test:
        data = {
            'message': 'Test no encontrado',
            'status': 404
        }
        
        return make_response(jsonify(data), 404)
    
    test.id_tipo_test = request.get_json().get('id_tipo_test')
    test.id_paciente = request.get_json().get('id_paciente')
    test.resultado = request.get_json().get('resultado')
    test.interpretacion = request.get_json().get('interpretacion')
    test.color = request.get_json().get('color')
    test.fecha = request.get_json().get('fecha')
    test.ansiedad_consignada = request.get_json().get('ansiedad_consignada')
    test.observaciones = request.get_json().get('observaciones')
    test.consignado = request.get_json().get('consignado')
    
    db.session.commit()
    
    data = {
        'message': 'Test actualizado con éxito',
        'status': 200,
        'test': test_schema.dump(test)
    }
    
    return make_response(jsonify(data), 200)

@tests.route('/tests/delete/<int:id_test>', methods=['DELETE'])
@jwt_required()
def delete(id_test):
    test = Test.query.get(id_test)
    
    if not test:
        data = {
            'message': 'Test no encontrado',
            'status': 404
        }
        
        return make_response(jsonify(data), 404)

    db.session.delete(test)
    db.session.commit()
    
    data = {
        'message': 'Test eliminado con éxito',
        'status': 200
    }
    
    return make_response(jsonify(data), 200)