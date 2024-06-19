from utils.db import db
from dataclasses import dataclass
from models.tipo_test import TipoTest

@dataclass
class Pregunta(db.Model):
    __tablename__ = 'pregunta'
    
    id_pregunta = db.Column(db.Integer, primary_key=True)
    id_tipo_test = db.Column(db.Integer, db.ForeignKey('tipo_test.id_tipo_test'))
    contenido = db.Column(db.String(255))

    respuesta = db.relationship('Respuesta', backref='pregunta', cascade='all, delete-orphan')
    
    def __init__(self,id_tipo_test,contenido):
        self.id_tipo_test = id_tipo_test
        self.contenido = contenido