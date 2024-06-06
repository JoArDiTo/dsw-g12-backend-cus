from flask import Blueprint, request, jsonify, make_response
from models.test import Test
from utils.db import db
from schemas.test_schema import test_schema, tests_schema

tests = Blueprint('tests', __name__)

@tests.route('/tests/get', methods=['GET'])
def get_tests():
    tests = Test.query.all()
    result = tests_schema.dump(tests)
    
    data = {
        'message': 'Lista generada con éxito',
        'status': 200,
        'tests': result
    }

    return make_response(jsonify(data), 200)

@tests.route('/tests/insert', methods=['POST'])
def insert():
    data = request.get_json()
    id_evaluacion = data.get('id_evaluacion')
    id_tipo_test = data.get('id_tipo_test')
    puntaje_total = data.get('puntaje_total')
    diagnostico = data.get('diagnostico')
    
    if not id_evaluacion or not id_tipo_test or not puntaje_total or not diagnostico:
        data = {
            'message': 'Faltan datos',
            'status': 400
        }
        
        return make_response(jsonify(data), 400)
    
    test = Test(id_evaluacion, id_tipo_test, puntaje_total, diagnostico)
    db.session.add(test)
    db.session.commit()
    
    result = test_schema.dump(test)
    
    data = {
        'message': 'Test creado con éxito',
        'status': 201,
        'data': result
    }
    
    return make_response(jsonify(result), 201) 

@tests.route('/tests/update/<int:id>', methods=['PUT'])
def update(id):
    data = request.get_json()
    test = Test.query.get(id)
    
    if test:
        test.id_evaluacion = data.get('id_evaluacion')
        test.id_tipo_test = data.get('id_tipo_test')
        test.puntaje_total = data.get('puntaje_total')
        test.diagnostico = data.get('diagnostico')
        db.session.commit()
        
        result = test_schema.dump(test)
        
        data = {
            'message': 'Test actualizado con éxito',
            'status': 200,
            'data': result
        }
        
        return make_response(jsonify(data), 200)
    
    data = {
        'message': 'Test no encontrado',
        'status': 404
    }
    
    return make_response(jsonify(data), 404)

#NO SE PUEDE ELIMINAR UN TEST PORQUE SE PIERDE LA RELACIÓN CON LAS PREGUNTAS Y RESPUESTAS
@tests.route('/tests/delete/<int:id>', methods=['DELETE'])
def delete(id):
    test = Test.query.get(id)
    
    if test:
        db.session.delete(test)
        db.session.commit()
        
        data = {
            'message': 'Test eliminado con éxito',
            'status': 200
        }
        
        return make_response(jsonify(data), 200)
    
    data = {
        'message': 'Test no encontrado',
        'status': 404
    }
    
    return make_response(jsonify(data), 404)