from flask import Flask
from utils.db import db
from config import DATABASE_CONNECTION
from flask_migrate import Migrate
from services.tipo_rol import roles
from services.usuario import usuarios
from services.estudiante import estudiantes
from services.especialista import especialistas
from services.historial_clinico import historial_clinico
from services.horario import horarios
from services.atencion import atenciones
from services.cita import citas
from services.evaluacion import evaluaciones
from services.tipo_test import tipos_test
from services.test import tests
from services.respuesta import respuestas
from services.pregunta import preguntas
from services.alternativa import alternativas
from services.escala_calificacion import escalas
from services.rango_calificacion import rangos
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from datetime import timedelta

app=Flask(__name__)

app.config['JWT_SECRET_KEY']='9aa6fe2ac33742958ef600ffea2230fc'
app.config['JWT_ACCESS_TOKEN_EXPIRES']=timedelta(hours=2)
app.config['JWT_REFRESH_TOKEN_EXPIRES']=timedelta(days=1)
jwt=JWTManager(app)

CORS(app, resources={r"/*": {"origins": "http://localhost:4200"}})
app.config['SQLALCHEMY_DATABASE_URI']=DATABASE_CONNECTION
db.init_app(app)

app.register_blueprint(roles)
app.register_blueprint(usuarios)
app.register_blueprint(estudiantes)
app.register_blueprint(especialistas)
app.register_blueprint(historial_clinico)
app.register_blueprint(horarios)
app.register_blueprint(atenciones)
app.register_blueprint(citas)
app.register_blueprint(evaluaciones)
app.register_blueprint(tipos_test)
app.register_blueprint(tests)
app.register_blueprint(respuestas)
app.register_blueprint(preguntas)
app.register_blueprint(alternativas)
app.register_blueprint(escalas)
app.register_blueprint(rangos)


with app.app_context():
    db.create_all()
    
    
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=5000)
