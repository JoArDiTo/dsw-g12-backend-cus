from flask import Blueprint, request, jsonify, make_response
from models.tipo_rol import TipoRol
from utils.db import db
from schemas.tipo_rol_schema import tipo_roles_schema, tipos_roles_schema

roles = Blueprint('roles', __name__)

@roles.route('/roles/get', methods=['GET'])
def get_roles():
    result = {}
    rols = TipoRol.query.all()
    result = tipos_roles_schema.dump(rols)
    
    data = {
        'message': 'Lista generada con éxito',
        'status': 200,
        'roles': result
    }

    return jsonify(data)

@roles.route('/roles/insert', methods=['POST'])
def insert():
    data = request.get_json()
    descripcion = data.get('descripcion')
    
    if not descripcion:
        data = {
            'message': 'Faltan datos',
            'status': 400
        }
        
        return make_response(jsonify(data), 400)
    
    rol = TipoRol(descripcion)
    db.session.add(rol)
    db.session.commit()
    
    result = tipo_roles_schema.dump(rol)
    
    data = {
        'message': 'Rol creado con éxito',
        'status': 201,
        'data': result
    }
    
    return jsonify(result)

@roles.route('/roles/update/<int:id>', methods=['PUT'])
def update(id):
    data = request.get_json()
    descripcion = data.get('descripcion')
    
    if not descripcion:
        data = {
            'message': 'Faltan datos',
            'status': 400
        }
        
        return make_response(jsonify(data), 400)
    
    rol = TipoRol.query.get(id)
    
    if not rol:
        data = {
            'message': 'Rol no encontrado',
            'status': 404
        }
        
        return make_response(jsonify(data), 404)
    
    rol.descripcion = descripcion
    db.session.commit()
    
    result = tipo_roles_schema.dump(rol)
    
    data = {
        'message': 'Rol actualizado con éxito',
        'status': 200,
        'data': result
    }
    
    return jsonify(data)

@roles.route('/roles/delete/<int:id>', methods=['DELETE'])
def delete(id):
    rol = TipoRol.query.get(id)
    
    if not rol:
        data = {
            'message': 'Rol no encontrado',
            'status': 404
        }
        
        return make_response(jsonify(data), 404)
    
    db.session.delete(rol)
    db.session.commit()
    
    data = {
        'message': 'Rol eliminado con éxito',
        'status': 200
    }
    
    return jsonify(data)