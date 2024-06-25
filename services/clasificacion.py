from flask import Blueprint, request, jsonify, make_response
from models.clasificacion import Clasificacion
from utils.db import db
from schemas.clasificacion_schema import clasificacion_schema, clasificaciones_schema
from flask_jwt_extended import jwt_required

clasificaciones = Blueprint('clasificaciones', __name__)

@clasificaciones.route('/clasificaciones/get', methods=['GET'])
@jwt_required()
def get_clasificaciones_calificacion():
    result = {}
    clasificaciones_calificacion = Clasificacion.query.all()
    result = clasificaciones_schema.dump(clasificaciones_calificacion)
    
    data = {
        'message': 'Lista generada con éxito',
        'status': 200,
        'clasificaciones': result
    }
    
    return make_response(jsonify(data), 200)

@clasificaciones.route('/clasificaciones/insert', methods=['POST'])
@jwt_required()
def insert():
    data = request.get_json()
    
    id_tipo_test = data.get('id_tipo_test')
    minimo = data.get('minimo')
    maximo = data.get('maximo')
    interpretacion = data.get('interpretacion')
    id_semaforo = data.get('id_semaforo')
    
    if id_tipo_test==None or minimo==None or maximo==None or interpretacion==None or id_semaforo==None:
        data = {
            'message': 'Faltan datos',
            'status': 400
        }
        
        return make_response(jsonify(data), 400)

    clasificacion = Clasificacion(id_tipo_test, minimo, maximo, interpretacion, id_semaforo)    
    db.session.add(clasificacion)
    db.session.commit()
    
    data = {
        'message': 'Rango de calificación creado con éxito',
        'status': 201,
        'clasificacion': clasificacion_schema.dump(clasificacion)
    }
    
    return make_response(jsonify(data), 201)

@clasificaciones.route('/clasificaciones/update/<int:id_clasificacion>', methods=['PUT'])
@jwt_required()
def update(id_clasificacion):
    clasificacion = Clasificacion.query.get(id_clasificacion)
    
    if not clasificacion:
        data = {
            'message': 'Rango de calificación no encontrado',
            'status': 404
        }
        
        return make_response(jsonify(data), 404)
    
    clasificacion.id_tipo_test = request.get_json().get('id_tipo_test')
    clasificacion.minimo = request.get_json().get('minimo')
    clasificacion.maximo = request.get_json().get('maximo')
    clasificacion.interpretacion = request.get_json().get('interpretacion')
    clasificacion.id_semaforo = request.get_json().get('id_semaforo')
    
    db.session.commit()
    
    data = {
        'message': 'Rango de calificación actualizado con éxito',
        'status': 200,
        'clasificacion': clasificacion_schema.dump(clasificacion)
    }
    
    return make_response(jsonify(data), 200)

@clasificaciones.route('/clasificaciones/delete/<int:id_clasificacion>', methods=['DELETE'])
@jwt_required()
def delete(id_clasificacion):
    clasificacion = Clasificacion.query.get(id_clasificacion)
    
    if not clasificacion:
        data = {
            'message': 'Clasificación no encontrada',
            'status': 404
        }
        
        return make_response(jsonify(data), 404)

    db.session.delete(clasificacion)
    db.session.commit()

    data = {
        'message': 'Clasificacion eliminada con éxito',
        'status': 200
    }
    
    return make_response(jsonify(data), 200)