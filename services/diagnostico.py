from schemas.diagnostico_schema import diagnostico_schema, diagnosticos_schema
from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import jwt_required
from models.diagnostico import Diagnostico
from utils.db import db

diagnosticos = Blueprint("diagnosticos", __name__)


@diagnosticos.route("/diagnosticos/get", methods=["GET"])
@jwt_required()
def get_diagnosticos():
    result = {}
    diagnosticos = Diagnostico.query.all()
    result = diagnosticos_schema.dump(diagnosticos)

    data = {"message": "Lista generada con éxito", "status": 200, "diagnosticos": result}

    return make_response(jsonify(data), 200)

@diagnosticos.route("/diagnosticos/get/<int:id_diagnostico>", methods=["GET"])
@jwt_required()
def get_diagnostico(id_diagnostico):
    diagnostico = Diagnostico.query.get(id_diagnostico)

    if not diagnostico:
        data = {"message": "No se encontró el diagnostico", "status": 404}

        return make_response(jsonify(data), 404)

    data = {
        "message": "Diagnostico encontrado con éxito",
        "status": 200,
        "diagnostico": diagnostico_schema.dump(diagnostico),
    }

    return make_response(jsonify(data), 200)


@diagnosticos.route("/diagnosticos/insert", methods=["POST"])
@jwt_required()
def insert():
    data = request.get_json()

    descripcion = data.get("descripcion")
    fundamentacion = data.get("fundamentacion")

    if descripcion == None or fundamentacion == None:
        data = {"message": "Faltan datos", "status": 400}

        return make_response(jsonify(data), 400)

    diagnostico = Diagnostico(descripcion, fundamentacion)
    db.session.add(diagnostico)
    db.session.commit()

    data = {
        "message": "Diagnostico creado con éxito",
        "status": 201,
        "diagnostico": diagnostico_schema.dump(diagnostico),
    }

    return make_response(jsonify(data), 201)


@diagnosticos.route("/diagnosticos/update/<int:id_diagnostico>", methods=["PUT"])
@jwt_required()
def update(id_diagnostico):
    diagnostico = Diagnostico.query.get(id_diagnostico)

    if not diagnostico:
        data = {"message": "No se encontró el diagnostico", "status": 404}

        return make_response(jsonify(data), 404)

    diagnostico.descripcion = request.get_json().get("descripcion")
    diagnostico.fundamentacion = request.get_json().get("fundamentacion")
    db.session.commit()

    data = {
        "message": "Diagnostico actualizado con éxito",
        "status": 200,
        "diagnostico": diagnostico_schema.dump(diagnostico),
    }

    return make_response(jsonify(data), 200)


@diagnosticos.route("/diagnosticos/delete/<int:id_diagnostico>", methods=["DELETE"])
@jwt_required()
def delete(id_diagnostico):
    diagnostico = Diagnostico.query.get(id_diagnostico)

    if not diagnostico:
        data = {"message": "No se encontró el diagnostico", "status": 404}

        return make_response(jsonify(data), 404)

    db.session.delete(diagnostico)
    db.session.commit()

    data = {"message": "Diagnostico eliminado con éxito", "status": 200}

    return make_response(jsonify(data), 200)
