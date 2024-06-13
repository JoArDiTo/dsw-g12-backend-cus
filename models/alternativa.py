from utils.db import db
from dataclasses import dataclass
from models.pregunta import TipoTest

@dataclass
class Alternativa(db.Model):
    __tablename__ = 'alternativa'
    
    id_alternativa = db.Column(db.Integer, primary_key=True)
    id_tipo_test = db.Column(db.Integer, db.ForeignKey('tipo_test.id_tipo_test'))
    texto = db.Column(db.String(100))
    puntaje = db.Column(db.Integer)
    
    def __init__(self, id_tipo_test, texto, puntaje):
        self.id_tipo_test = id_tipo_test
        self.texto = texto
        self.puntaje = puntaje