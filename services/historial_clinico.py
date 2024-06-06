from flask import Blueprint, request, jsonify, make_response
from models.historial_clinico import HistorialClinico
from utils.db import db
from schemas.historial_clinico_schema import historial_clinico_schema, historiales_clinicos_schema

historial_clinico = Blueprint('historial_clinico', __name__)

@historial_clinico.route('/historiales/get', methods=['GET'])
def get_historiales():
    historiales = HistorialClinico.query.all()
    result = historiales_clinicos_schema.dump(historiales)
    
    data = {
        'message': 'Lista generada con éxito',
        'status': 200,
        'historiales': result
    }

    return make_response(jsonify(data), 200)

@historial_clinico.route('/historiales/insert', methods=['POST'])
def insert():
    data = request.get_json()
    cod_alumno = data.get('cod_alumno')
    id_especialista = data.get('id_especialista')
    
    if not cod_alumno or not id_especialista:
        data = {
            'message': 'Faltan datos',
            'status': 400
        }
        
        return make_response(jsonify(data), 400)
    
    historial = HistorialClinico(cod_alumno, id_especialista)
    db.session.add(historial)
    db.session.commit()
    
    result = historial_clinico_schema.dump(historial)
    
    data = {
        'message': 'Historial creado con éxito',
        'status': 201,
        'data': result
    }
    
    return make_response(jsonify(data), 201)

#NO SE PUEDE ACTUALIZAR UN HISTORIAL CLINICO, DEBIDO A QUE ES ÚNICO PARA CADA ESTUDIANTE
@historial_clinico.route('/historiales/update/<int:id>', methods=['PUT'])
def update(id):
    data = request.get_json()
    historial = HistorialClinico.query.get(id)
    
    if historial:
        cod_alumno = data.get('cod_alumno')
        id_especialista = data.get('id_especialista')
        
        if cod_alumno:
            historial.cod_alumno = cod_alumno
        if id_especialista:
            historial.id_especialista = id_especialista
        
        db.session.commit()
        
        result = historial_clinico_schema.dump(historial)
        
        data = {
            'message': 'Historial actualizado con éxito',
            'status': 200,
            'data': result
        }
        
        return make_response(jsonify(data), 200)
    
    data = {
        'message': 'Historial no encontrado',
        'status': 404
    }
    
    return make_response(jsonify(data), 404)


@historial_clinico.route('/historiales/delete/<int:id>', methods=['DELETE'])
def delete(id):
    result = {}
    historial = HistorialClinico.query.get(id)
    
    if historial:
        db.session.delete(historial)
        db.session.commit()
        
        result = historial_clinico_schema.dump(historial)
        
        data = {
            'message': 'Historial eliminado con éxito',
            'status': 200,
            'data': result
        }
        
        return make_response(jsonify(data), 200)
    
    data = {
        'message': 'Historial no encontrado',
        'status': 404
    }
    
    return make_response(jsonify(data), 404)