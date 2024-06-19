from flask import Flask
from utils.db import db
from config import DATABASE_CONNECTION
from flask_migrate import Migrate
from services.ubigeo import ubigeos
from services.persona import personas
from services.usuario import usuarios
from services.paciente import pacientes
from services.especialista import especialistas
from services.cita import citas
from services.resultado_cita import resultados
from services.tipo_test import tipos_test
from services.test import tests
from services.respuesta import respuestas
from services.pregunta import preguntas
from services.alternativa import alternativas
from services.semaforo import semaforos
from services.clasificacion import clasificaciones
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from datetime import timedelta

app=Flask(__name__)

app.config['SECRET_KEY']='97017582b69247b8a8a88491e108c1ca'
app.config['JWT_SECRET_KEY']='9aa6fe2ac33742958ef600ffea2230fc'
app.config['JWT_ACCESS_TOKEN_EXPIRES']=timedelta(hours=2)
app.config['JWT_REFRESH_TOKEN_EXPIRES']=timedelta(days=1)

jwt=JWTManager(app)

CORS(app, resources={r"/*": {"origins": "http://localhost:4200"}})
app.config['SQLALCHEMY_DATABASE_URI']=DATABASE_CONNECTION
db.init_app(app)

app.register_blueprint(ubigeos)
app.register_blueprint(personas)
app.register_blueprint(usuarios)
app.register_blueprint(pacientes)
app.register_blueprint(especialistas)
app.register_blueprint(citas)
app.register_blueprint(resultados)
app.register_blueprint(tipos_test)
app.register_blueprint(tests)
app.register_blueprint(respuestas)
app.register_blueprint(preguntas)
app.register_blueprint(alternativas)
app.register_blueprint(semaforos)
app.register_blueprint(clasificaciones)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=5000)
