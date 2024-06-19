from flask import Blueprint, request, jsonify, make_response
from models.ubigeo import Ubigeo
from utils.db import db
from schemas.ubigeo_schema import ubigeo_schema, ubigeos_schema
from flask_jwt_extended import jwt_required


ubigeos = Blueprint('ubigeos', __name__)

@ubigeos.route('/ubigeos/get', methods=['GET'])
@jwt_required()
def get_ubigeos():
    result = {}
    ubigeos = Ubigeo.query.all()
    result = ubigeos_schema.dump(ubigeos)
    
    data = {
        'message': 'Lista generada con éxito',
        'status': 200,
        'ubigeos': result
    }
    
    return make_response(jsonify(data),200)

@ubigeos.route('/ubigeos/insert', methods=['POST'])
# @jwt_required()
def insert():
    data = request.get_json()
    
    id_ubigeo = data.get('id_ubigeo')
    departamento = data.get('departamento')
    provincia = data.get('provincia')
    distrito = data.get('distrito')
    superficie = data.get('superficie')
    altitud = data.get('altitud')
    latitud = data.get('latitud')
    
    if id_ubigeo==None or departamento==None or provincia==None or distrito==None or superficie==None or altitud==None or latitud==None:
        data = {
            'message': 'Faltan datos',
            'status': 400
        }
        
        return make_response(jsonify(data),400)
    
    ubigeo = Ubigeo(id_ubigeo, departamento, provincia, distrito, superficie, altitud, latitud)
    
    db.session.add(ubigeo)
    db.session.commit()
    
    data = {
        'message': 'Ubigeo creado con éxito',
        'status': 200,
        'ubigeo': ubigeo_schema.dump(ubigeo)
    }
    
    return make_response(jsonify(data),200)

@ubigeos.route('/ubigeos/update/<string:id_ubigeo>', methods=['PUT'])
@jwt_required()
def update(id_ubigeo):    
    ubigeo = Ubigeo.query.get(id_ubigeo)
    
    if ubigeo==None:
        data = {
            'message': 'Ubigeo no encontrado',
            'status': 400
        }
        
        return make_response(jsonify(data),400)
    
    ubigeo.departamento = request.json.get('departamento')
    ubigeo.provincia = request.json.get('provincia')
    ubigeo.distrito = request.json.get('distrito')
    ubigeo.superficie = request.json.get('superficie')
    ubigeo.altitud = request.json.get('altitud')
    ubigeo.latitud = request.json.get('latitud')
    
    db.session.commit()
    
    data = {
        'message': 'Ubigeo actualizado con éxito',
        'status': 200,
        'ubigeo': ubigeo_schema.dump(ubigeo)
    }
    
    return make_response(jsonify(data),200)

@ubigeos.route('/ubigeos/delete/<string:id_ubigeo>', methods=['DELETE'])
@jwt_required()
def delete(id_ubigeo):    
    ubigeo = Ubigeo.query.get(id_ubigeo)
    
    if not ubigeo:
        data = {
            'message': 'Ubigeo no encontrado',
            'status': 400
        }
        
        return make_response(jsonify(data),400)
    
    db.session.delete(ubigeo)
    db.session.commit()
    
    data = {
        'message': 'Ubigeo eliminado con éxito',
        'status': 200,
        'ubigeo': ubigeo_schema.dump(ubigeo)
    }
    
    return make_response(jsonify(data),200)