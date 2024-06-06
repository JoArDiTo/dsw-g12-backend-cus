from flask import Blueprint, request, jsonify, make_response
from models.usuario import Usuario
from utils.db import db
from schemas.usuario_schema import usuario_schema, usuarios_schema
from werkzeug.security import generate_password_hash, check_password_hash

usuarios = Blueprint('usuarios', __name__)

@usuarios.route('/usuarios/login', methods=['POST'])
def login():
    data = request.get_json()
    correo = data.get('correo')
    password = data.get('password')
    
    usuario = Usuario.query.filter_by(correo=correo).first()
    
    if not usuario:
        data = {
            'message': 'Usuario no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    
    if not check_password_hash(usuario.password, password):
        data = {
            'message': 'Contraseña incorrecta',
            'status': 400
        }
        return make_response(jsonify(data), 400)
    
    result = usuario_schema.dump(usuario)
    
    data = {
        'message': 'Usuario encontrado con éxito',
        'status': 200,
        'data': result
    }
    
    return make_response(jsonify(data), 200)

@usuarios.route('/usuarios/get', methods=['GET'])
def get_usuarios():
    result = {}
    usuarios = Usuario.query.all()
    result = usuarios_schema.dump(usuarios)
    
    data = {
        'message': 'Lista generada con éxito',
        'status': 200,
        'usuarios': result
    }

    return make_response(jsonify(data),200)

@usuarios.route('/usuarios/insert', methods=['POST'])
def insert():
    data = request.get_json()
    documento = data.get('documento')
    tipo_documento = data.get('tipo_documento')
    nombre = data.get('nombre')
    apellido_paterno = data.get('apellido_paterno')
    apellido_materno = data.get('apellido_materno')
    telefono = data.get('telefono')
    correo = data.get('correo')
    password = data.get('password')
    id_tipo_rol = data.get('id_tipo_rol')

    if not documento or not tipo_documento or not nombre or not apellido_paterno or not apellido_materno or not telefono or not correo or not password or not id_tipo_rol:
        data = {
            'message': 'Faltan datos',
            'status': 400
        }
        
        return make_response(jsonify(data), 400)

    new_usuario = Usuario(documento,tipo_documento,nombre,apellido_paterno,apellido_materno,telefono,correo,password,id_tipo_rol)    
    db.session.add(new_usuario)
    db.session.commit()
    
    result = usuario_schema.dump(new_usuario)
    
    data = {
        'message': 'Usuario creada con éxito',
        'status': 201,
        'data': result
    }
    
    return make_response(jsonify(result),201)

@usuarios.route('/usuarios/update/<string:documento>', methods=['PUT'])
def update(documento):
    result = {}
    data = request.get_json()
    usuario = Usuario.query.get(documento)
    
    if not usuario:
        result['message'] = 'Usuario no encontrada'
        result['status'] = 404
        return make_response(jsonify(result), 404)
    
    usuario.tipo_documento = data.get('tipo_documento')
    usuario.nombre = data.get('nombre')
    usuario.apellido_paterno = data.get('apellido_paterno')
    usuario.apellido_materno = data.get('apellido_materno')
    usuario.telefono = data.get('telefono')
    usuario.correo = data.get('correo')
    usuario.password = data.get('password')
    usuario.id_tipo_rol = data.get('id_tipo_rol')
    
    db.session.commit()
    
    result = usuario_schema.dump(usuario)
    
    data = {
        'message': 'Usuario actualizada con éxito',
        'status': 200,
        'data': result
    }
    
    return make_response(jsonify(data), 200)


@usuarios.route('/usuarios/delete/<string:documento>', methods=['DELETE'])
def delete(documento):
    usuario = Usuario.query.get(documento)
    
    if not usuario:
        data = {
            'message': 'Usuario no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    
    result = usuario_schema.dump(usuario)
    
    db.session.delete(usuario)
    db.session.commit()
    
    data = {
        'message': 'Usuario eliminada con éxito',
        'status': 200,
        'data': result
    }
    
    return make_response(jsonify(data), 200)