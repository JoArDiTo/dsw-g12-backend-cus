from flask import Blueprint, request, jsonify, make_response
from models.estudiante import Estudiante
from utils.db import db
from schemas.estudiante_schema import estudiante_schema, estudiantes_schema
from flask_jwt_extended import jwt_required

estudiantes = Blueprint('estudiantes', __name__)

@estudiantes.route('/estudiantes/get', methods=['GET'])
@jwt_required()
def get_estudiantes():
    result = {}
    estudiantes = Estudiante.query.all()
    result = estudiantes_schema.dump(estudiantes)
    
    data = {
        'message': 'Lista generada con éxito',
        'status': 200,
        'estudiantes': result
    }
    
    return make_response(jsonify(data),200)
    

@estudiantes.route('/estudiantes/insert', methods=['POST'])
# NO SE REQUIERE JWT CREAR ESTUDIANTES
def insert():
    cod_alumno = request.json.get('cod_alumno')
    anio_ingreso = request.json.get('anio_ingreso')
    ciclo_estudio = request.json.get('ciclo_estudio')
    base = request.json.get('base')
    facultad = request.json.get('facultad')
    carrera = request.json.get('carrera')
    documento = request.json.get('documento')
    
    if Estudiante.query.get(cod_alumno):
        data = {
            'message':'Estudiante ya existe',
            'status': 400
        }
        
        return make_response(jsonify(data),400)
    
    if not cod_alumno or not anio_ingreso or not ciclo_estudio or not base or not facultad or not carrera or not documento:
        data = {
            'message':'Faltan datos',
            'status': 400
        }
        
        return make_response(jsonify(data),400)
    
    new_estudiante = Estudiante(cod_alumno, anio_ingreso, ciclo_estudio, base, facultad, carrera, documento)
    
    db.session.add(new_estudiante)
    db.session.commit()
    
    result = estudiante_schema.dump(new_estudiante)
    
    data = {
        'message':'Estudiante creado con éxito',
        'status': 201,
        'estudiante': result
    }
    
    return make_response(jsonify(data),201)


@estudiantes.route('/estudiantes/update/<int:cod_alumno>', methods=['PUT'])
@jwt_required()
def update(cod_alumno):
    estudiante = Estudiante.query.get(cod_alumno)
    
    if estudiante:
        estudiante.anio_ingreso = request.json.get('anio_ingreso')
        estudiante.ciclo_estudio = request.json.get('ciclo_estudio')
        estudiante.base = request.json.get('base')
        estudiante.facultad = request.json.get('facultad')
        estudiante.carrera = request.json.get('carrera')
        estudiante.documento = request.json.get('documento')
        
        db.session.commit()
        
        result = estudiante_schema.dump(estudiante)
        
        data = {
            'message':'Estudiante actualizado con éxito',
            'status': 200,
            'estudiante': result
        }
        
        return make_response(jsonify(data),200)
    
    data = {
        'message':'Estudiante no encontrado',
        'status': 404
    }
    
    return make_response(jsonify(data),404)

@estudiantes.route('/estudiantes/delete/<int:cod_alumno>', methods=['DELETE'])
@jwt_required()
def delete(cod_alumno):
    estudiante = Estudiante.query.get(cod_alumno)
    
    if estudiante:
        db.session.delete(estudiante)
        db.session.commit()
        
        data = {
            'message':'Estudiante eliminado con éxito',
            'status': 200
        }
        
        return make_response(jsonify(data),200)
    
    data = {
        'message':'Estudiante no encontrado',
        'status': 404
    }
    
    return make_response(jsonify(data),404)
