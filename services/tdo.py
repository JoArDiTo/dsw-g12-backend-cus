from models.pregunta import Pregunta
from models.alternativa import Alternativa
from models.test import Test
from models.respuesta import Respuesta
from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import jwt_required
from utils.db import db

tdo = Blueprint('tdo', __name__)

@tdo.route('/tdo/preguntas-y-alternativas/get/<int:id_tipo_test>', methods=['GET'])
def get_preguntas_y_alternativas(id_tipo_test):
    result = {}
    preguntas = Pregunta.query.filter_by(id_tipo_test=id_tipo_test).all()
    alternativas = Alternativa.query.filter_by(id_tipo_test=id_tipo_test).all()
    result['preguntas'] = [pregunta.contenido for pregunta in preguntas]
    result['alternativas'] = [
        {
            'contenido': alternativa.contenido, 'puntaje': alternativa.puntaje
        } for alternativa in alternativas
    ]

    data = {
        'message': 'Lista generada con éxito',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@tdo.route('/tdo/test-resumen/get/<int:id_test>', methods=['GET'])
def get_resumen(id_test):
    respuestas = Respuesta.query.filter_by(id_test=id_test).all()
    test = Test.query.filter_by(id_test=id_test).first()
    alternativas_marcadas = []
    preguntas_planteadas = []
    alternativas_dict = {alternativa.id_alternativa: alternativa.contenido for alternativa in Alternativa.query.filter_by(id_tipo_test=test.id_tipo_test).all()}
    preguntas_dict = {pregunta.id_pregunta: pregunta.contenido for pregunta in Pregunta.query.filter_by(id_tipo_test=test.id_tipo_test).all()}
    
    for respuesta in respuestas:
        alternativas_marcadas.append(alternativas_dict.get(respuesta.id_alternativa))
        preguntas_planteadas.append(preguntas_dict.get(respuesta.id_pregunta))
        
    data = {
        'message': 'Resumen generado con éxito',
        'status': 200,
        'resumen': {
            'preguntas_planteadas': preguntas_planteadas,
            'alternativas_marcadas': alternativas_marcadas
        }
    }

    return make_response(jsonify(data), 200)

from models.paciente import Paciente
from models.usuario import Usuario
from models.persona import Persona
from models.tipo_test import TipoTest
from models.clasificacion import Clasificacion
from models.semaforo import Semaforo
from sqlalchemy.orm import selectinload

@tdo.route('/tdo/tests-vigilancia/get', methods=['GET'])
def get_test_vigilancia():    
    tests = Test.query.options(
        selectinload(Test.tipo_test),
        selectinload(Test.clasificacion).selectinload(Clasificacion.semaforo),
        selectinload(Test.paciente).selectinload(Paciente.usuario).selectinload(Usuario.persona)
    ).filter(
        Test.id_tipo_test == TipoTest.id_tipo_test,
        Test.id_paciente == Paciente.id_paciente,
        Paciente.id_usuario == Usuario.id_usuario,
        Usuario.documento == Persona.documento
    ).all()
    
    tests_vigilancia = [
        {   
            "id_test": test.id_test,
            "Tipo de Test": test.tipo_test.nombre,
            "Paciente": f"{test.paciente.usuario.persona.nombre} {test.paciente.usuario.persona.apellido_paterno} {test.paciente.usuario.persona.apellido_materno}",
            "Fecha de Test": str(test.fecha),
            "Resultado": test.resultado,
            "color":test.clasificacion.semaforo.color,
            "Consignacion": test.id_vigilancia
        }
        for test in tests
    ]
    
    data = {
        'message': 'Lista generada con éxito',
        'status': 200,
        'tests': tests_vigilancia
    }
    return make_response(jsonify(data), 200)

from models.ubigeo import Ubigeo

@tdo.route('/tdo/tests-mapa/get', methods=['GET'])
def get_test_mapa():
    tests = Test.query.options(
        selectinload(Test.tipo_test),
        selectinload(Test.clasificacion).selectinload(Clasificacion.semaforo),
        selectinload(Test.paciente).selectinload(Paciente.usuario).selectinload(Usuario.persona).selectinload(Persona.ubigeo)
    ).filter(
        Test.id_tipo_test == TipoTest.id_tipo_test,
        Test.id_clasificacion == Clasificacion.id_clasificacion,
        Clasificacion.id_semaforo == Semaforo.id_semaforo,
        Test.id_paciente == Paciente.id_paciente,
        Paciente.id_usuario == Usuario.id_usuario,
        Usuario.documento == Persona.documento,
        Persona.id_ubigeo == Ubigeo.id_ubigeo
    ).all()
    
    tests_mapa = [
        {
            "ubigeo": test.paciente.usuario.persona.ubigeo.id_ubigeo,
            "Latitud": float(test.paciente.usuario.persona.ubigeo.latitud),
            "Longitud": float(test.paciente.usuario.persona.ubigeo.longitud),
            "distrito": test.paciente.usuario.persona.ubigeo.distrito,
            "color": test.clasificacion.semaforo.color,
            "Tipo de Test": test.tipo_test.nombre,
            "id_vigilancia": test.id_vigilancia
        }
        for test in tests
    ]
    
    data = {
        'message': 'Lista generada con éxito',
        'status': 200,
        'tests': tests_mapa
    }
    return make_response(jsonify(data), 200)