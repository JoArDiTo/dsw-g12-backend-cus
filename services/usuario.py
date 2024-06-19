from flask import Blueprint, request, jsonify, make_response
from models.usuario import Usuario
from utils.db import db
from schemas.usuario_schema import usuario_schema, usuarios_schema
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required

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
    
    
    
    data = {
        'message': 'Inicio de sesión exitoso',
        'access_token': create_access_token(identity=usuario.documento, additional_claims={"id_usuario": usuario.id_usuario}),
        'refresh_token': create_refresh_token(identity=usuario.documento),
    }
    
    return make_response(jsonify(data), 200)

@usuarios.route('/usuarios/validator', methods=['GET'])
def validator_email():
    correo = request.args.get('correo')
    usuario = Usuario.query.filter_by(correo=correo).first()
    
    if usuario:
        data = {
            'message': 'Correo ya registrado',
            'status': 400
        }
        return make_response(jsonify(data), 400)
    
    data = {
        'message': 'Correo disponible',
        'status': 200
    }
    
    return make_response(jsonify(data), 200)

@usuarios.route('/usuarios/get', methods=['GET'])
@jwt_required()
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
#NO SE DEBE REQUERIR JWT PARA CREAR UN USUARIO
def insert():
    data = request.get_json()
    
    documento = data.get('documento')
    correo = data.get('correo')
    password = data.get('password')
    
    if documento==None or correo==None or password==None:
        data = {
            'message': 'Faltan datos',
            'status': 400
        }
        
        return make_response(jsonify(data),400)
    
    usuario = Usuario(documento,correo,password)
    
    db.session.add(usuario)
    db.session.commit()
    
    data = {
        'message': 'Usuario creado con éxito',
        'status': 200,
        'usuario': usuario_schema.dump(usuario)
    }
    
    return make_response(jsonify(data),200)

@usuarios.route('/usuarios/update/<int:id_usuario>', methods=['PUT'])
@jwt_required()
def update(id_usuario):    
    usuario = Usuario.query.get(id_usuario)
    
    if usuario==None:
        data = {
            'message': 'Usuario no encontrada',
            'status': 400
        }
        
        return make_response(jsonify(data), 404)
    
    #usuario.id_usuario = request.json.get('id_usuario')
    #usuario.documento = request.json.get('documento')
    usuario.correo = request.json.get('correo')
    usuario.password = generate_password_hash(request.json.get('password'))
    
    db.session.commit()
    
    data = {
        'message': 'Usuario actualizada con éxito',
        'status': 200,
        'data': usuario_schema.dump(usuario)
    }
    
    return make_response(jsonify(data), 200)


@usuarios.route('/usuarios/delete/<int:id_usuario>', methods=['DELETE'])
@jwt_required()
def delete(id_usuario):
    usuario = Usuario.query.get(id_usuario)
    
    if not usuario:
        data = {
            'message': 'Usuario no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    
    db.session.delete(usuario)
    db.session.commit()
    
    data = {
        'message': 'Usuario eliminada con éxito',
        'status': 200,
        'data': usuario_schema.dump(usuario)
    }
    
    return make_response(jsonify(data), 200)