from flask import Blueprint, request, jsonify, make_response
from models.test import Test
from models.clasificacion import Clasificacion
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

@tests.route('/tests/get/<int:id_paciente>', methods=['GET'])
@jwt_required()
def get_tests_paciente(id_paciente):
    result = {}
    tests = Test.query.filter_by(id_paciente=id_paciente).all()
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
    puntajes = data.get('puntajes')
    fecha = data.get('fecha')
    id_vigilancia = data.get('id_vigilancia')

    resultado = 0
    for puntaje in puntajes:
        resultado += puntaje
    
    id_clasificacion = Clasificacion.query.filter(Clasificacion.id_tipo_test == id_tipo_test, Clasificacion.minimo <= resultado, Clasificacion.maximo >= resultado).first().id_clasificacion
    
    test = Test(id_tipo_test, id_paciente, id_clasificacion, resultado, fecha, id_vigilancia)
    db.session.add(test)
    db.session.commit()
    
    new_test = {
        "id_test": test.id_test,
        "clasificacion": Clasificacion.query.get(test.id_clasificacion).interpretacion,
    }
    
    data = {
        'message': 'Test creado con éxito',
        'status': 201,
        'test': new_test
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
    
    test.id_tipo_test = request.json.get('id_tipo_test', test.id_tipo_test)
    test.id_paciente = request.json.get('id_paciente', test.id_paciente)
    test.id_clasificacion = request.json.get('id_clasificacion', test.id_clasificacion)
    test.resultado = request.json.get('resultado', test.resultado)
    test.fecha = request.json.get('fecha', test.fecha)
    test.id_vigilancia = request.json['id_vigilancia']
    
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