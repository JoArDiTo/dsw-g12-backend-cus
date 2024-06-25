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
    resultado = db.Column(db.Integer)
    interpretacion = db.Column(db.String(255))
    fecha = db.Column(db.DateTime)
    color = db.Column(db.String(6))
    ansiedad_consignada = db.Column(db.String(255))
    observaciones = db.Column(db.String(255))
    consignado = db.Column(db.Boolean)
    
    respuesta = db.relationship('Respuesta', backref='test', cascade='all, delete-orphan')
    
    def __init__(self,id_tipo_test,id_paciente,resultado,interpretacion, color, fecha):
        self.id_tipo_test = id_tipo_test
        self.id_paciente = id_paciente
        self.resultado = resultado
        self.interpretacion = interpretacion
        self.color = color
        self.fecha = fecha
        self.ansiedad_consignada = "Por consignar"
        self.observaciones = "Por detallar"
        self.consignado = False