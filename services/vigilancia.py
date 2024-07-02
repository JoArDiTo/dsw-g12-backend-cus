from schemas.vigilancia_schema import vigilancia_schema, vigilancias_schema
from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import jwt_required
from models.vigilancia import Vigilancia
from utils.db import db

vigilancias = Blueprint('vigilancias', __name__)

@vigilancias.route('/vigilancias/get', methods=['GET'])
@jwt_required()
def get_vigilancias():
    result = {}
    vigilancias = Vigilancia.query.all()
    result = vigilancias_schema.dump(vigilancias)
    
    data = {
        'message': 'Lista generada con éxito',
        'status': 200,
        'vigilancias': result
    }

    return make_response(jsonify(data), 200)
  
@vigilancias.route('/vigilancias/insert', methods=['POST'])
@jwt_required()
def insert():
    data = request.get_json()
    
    id_diagnostico = data.get('id_diagnostico')
    id_tratamiento = data.get('id_tratamiento')
    observacion = data.get('observacion')
    fundamentacion = data.get('fundamentacion')
    
    if id_diagnostico==None or id_tratamiento==None or observacion==None or fundamentacion==None:
        data = {
            'message': 'Faltan datos',
            'status': 400
        }
        
        return make_response(jsonify(data), 400)
      
    vigilancia = Vigilancia(id_diagnostico, id_tratamiento, observacion, fundamentacion)
    db.session.add(vigilancia)
    db.session.commit()
    
    data = {
        'message': 'Vigilancia creada con éxito',
        'status': 201,
        'vigilancia': vigilancia_schema.dump(vigilancia)
    }
    
    return make_response(jsonify(data), 201)
  
@vigilancias.route('/vigilancias/update/<int:id_vigilancia>', methods=['PUT'])
@jwt_required()
def update(id_vigilancia):
    vigilancia = Vigilancia.query.get(id_vigilancia)
    
    if not vigilancia:
        data = {
            'message': 'No se encontró la vigilancia',
            'status': 404
        }
        
        return make_response(jsonify(data), 404)
    
    vigilancia.id_diagnostico = request.json['id_diagnostico']
    vigilancia.id_tratamiento = request.json['id_tratamiento']
    vigilancia.observacion = request.json['observacion']
    vigilancia.fundamentacion = request.json['fundamentacion']
    
    db.session.commit()
    
    data = {
        'message': 'Vigilancia actualizada con éxito',
        'status': 200,
        'vigilancia': vigilancia_schema.dump(vigilancia)
    }
    
    return make_response(jsonify(data), 200)
  
@vigilancias.route('/vigilancias/delete/<int:id_vigilancia>', methods=['DELETE'])
@jwt_required()
def delete(id_vigilancia):
    vigilancia = Vigilancia.query.get(id_vigilancia)
    
    if not vigilancia:
        data = {
            'message': 'No se encontró la vigilancia',
            'status': 404
        }
        
        return make_response(jsonify(data), 404)
    
    db.session.delete(vigilancia)
    db.session.commit()
    
    data = {
        'message': 'Vigilancia eliminada con éxito',
        'status': 200
    }
    
    return make_response(jsonify(data), 200)