from utils.db import db
from dataclasses import dataclass
from models.test import Test

@dataclass
class Respuesta(db.Model):
    __tablename__ = 'respuesta'
    
    id_respuesta = db.Column(db.Integer, primary_key=True)
    id_test = db.Column(db.Integer, db.ForeignKey('test.id_test'))
    pregunta = db.Column(db.String(256))
    respuesta = db.Column(db.Integer)
    puntaje = db.Column(db.Integer)
        
    def __init__(self, id_test, pregunta, respuesta, puntaje):
        self.id_test = id_test
        self.pregunta = pregunta
        self.respuesta = respuesta
        self.puntaje = puntaje