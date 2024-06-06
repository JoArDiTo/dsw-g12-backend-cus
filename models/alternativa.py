from utils.db import db
from dataclasses import dataclass
from models.pregunta import Pregunta

@dataclass
class Alternativa(db.Model):
    __tablename__ = 'alternativa'
    
    id_alternativa = db.Column(db.Integer, primary_key=True)
    id_pregunta = db.Column(db.Integer, db.ForeignKey('pregunta.id_pregunta'))
    texto = db.Column(db.String(100))
    puntaje = db.Column(db.Integer)
    
    def __init__(self, id_pregunta, texto, puntaje):
        self.id_pregunta = id_pregunta
        self.texto = texto
        self.puntaje = puntaje