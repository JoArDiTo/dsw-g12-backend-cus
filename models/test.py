from utils.db import db
from dataclasses import dataclass
from models.tipo_test import TipoTest
from models.paciente import Paciente
import datetime

@dataclass
class Test(db.Model):
    __tablename__ = 'test'
    
    id_test = db.Column(db.Integer, primary_key=True)
    id_tipo_test = db.Column(db.Integer, db.ForeignKey('tipo_test.id_tipo_test'))
    id_paciente = db.Column(db.Integer, db.ForeignKey('paciente.id_paciente'))
    id_clasificacion = db.Column(db.Integer, db.ForeignKey('clasificacion.id_clasificacion'))
    resultado = db.Column(db.Integer)
    fecha = db.Column(db.DateTime)
    id_vigilancia = db.Column(db.Integer, db.ForeignKey('vigilancia.id_vigilancia'))
    
    respuesta = db.relationship('Respuesta', backref='test', cascade='all, delete-orphan')
    
    def __init__(self, id_tipo_test, id_paciente, id_clasificacion, resultado, fecha, id_vigilancia):
        self.id_tipo_test = id_tipo_test
        self.id_paciente = id_paciente
        self.id_clasificacion = id_clasificacion
        self.resultado = resultado
        self.fecha = fecha
        self.id_vigilancia = id_vigilancia