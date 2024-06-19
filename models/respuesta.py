from utils.db import db
from dataclasses import dataclass
from models.test import Test
from models.pregunta import Pregunta
from models.alternativa import Alternativa

@dataclass
class Respuesta(db.Model):
    __tablename__ = 'respuesta'
    
    id_respuesta = db.Column(db.Integer, primary_key=True)
    id_test = db.Column(db.Integer, db.ForeignKey('test.id_test'))
    id_pregunta = db.Column(db.Integer, db.ForeignKey('pregunta.id_pregunta'))
    id_alternativa = db.Column(db.Integer, db.ForeignKey('alternativa.id_alternativa'))
    
    def __init__(self, id_test, id_pregunta, id_alternativa):
        self.id_test = id_test
        self.id_pregunta = id_pregunta
        self.id_alternativa = id_alternativa