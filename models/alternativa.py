from utils.db import db
from dataclasses import dataclass
from models.pregunta import TipoTest

@dataclass
class Alternativa(db.Model):
    __tablename__ = 'alternativa'
    
    id_alternativa = db.Column(db.Integer, primary_key=True)
    id_tipo_test = db.Column(db.Integer, db.ForeignKey('tipo_test.id_tipo_test'))
    contenido = db.Column(db.String(255))
    puntaje = db.Column(db.Integer)
    
    respuesta = db.relationship('Respuesta', backref='alternativa', cascade='all, delete-orphan')
    
    def __init__(self, id_tipo_test, contenido,puntaje):
        self.id_tipo_test = id_tipo_test
        self.contenido = contenido
        self.puntaje = puntaje