from flask import Blueprint, request, jsonify, make_response
from models.resultado_cita import ResultadoCita
from utils.db import db
from schemas.resultado_cita_schema import resultado_cita_schema, resultados_cita_schema
from flask_jwt_extended import jwt_required

resultados = Blueprint('resultados', __name__)

@resultados.route('/resultados/get', methods=['GET'])
@jwt_required()
def get_resultados():
    result = {}
    resultados = ResultadoCita.query.all()
    result = resultados_cita_schema.dump(resultados)
    
    data = {
        'message': 'Lista generada con éxito',
        'status': 200,
        'resultados': result
    }

    return make_response(jsonify(data), 200)

@resultados.route('/resultados/insert', methods=['POST'])
@jwt_required()
def insert():
    data = request.get_json()
    
    id_cita = data.get('id_cita')
    observacion = data.get('observacion')
    tratamiento = data.get('tratamiento')
    
    if id_cita==None or observacion==None or tratamiento==None:
        data = {
            'message': 'Faltan datos',
            'status': 400
        }
        
        return make_response(jsonify(data), 400)
    
    resultado = ResultadoCita(id_cita, observacion, tratamiento)
    db.session.add(resultado)
    db.session.commit()
    
    data = {
        'message': 'Resultado creado con éxito',
        'status': 201,
        'data': resultado_cita_schema.dump(resultado)
    }
    
    return make_response(jsonify(data), 201)

@resultados.route('/resultados/update/<int:id_resultado>', methods=['PUT'])
@jwt_required()
def update(id_resultado):
    resultado = ResultadoCita.query.get(id_resultado)
    
    if resultado == None:
        data = {
            'message': 'Resultado no encontrado',
            'status': 400
        }
        
        return make_response(jsonify(data), 400)
    
    # resultado.id_cita = data.get('id_cita', resultado.id_cita)
    resultado.observacion = request.get_json().get('observacion')
    resultado.tratamiento = request.get_json().get('tratamiento')
    
    db.session.commit()
    
    data = {
        'message': 'Resultado actualizado con éxito',
        'status': 200,
        'data': resultado_cita_schema.dump(resultado)
    }
    
    return make_response(jsonify(data), 200)

@resultados.route('/resultados/delete/<int:id_resultado>', methods=['DELETE'])
@jwt_required()
def delete(id_resultado):
    resultado = ResultadoCita.query.get(id_resultado)
    
    if resultado == None:
        data = {
            'message': 'Resultado no encontrado',
            'status': 404
        }
        
        return make_response(jsonify(data), 404)
    
    db.session.delete(resultado)
    db.session.commit()
    
    data = {
        'message': 'Resultado eliminado con éxito',
        'status': 200,
        'data': resultado_cita_schema.dump(resultado)
    }
    
    return make_response(jsonify(data), 200)