from utils.db import db
from dataclasses import dataclass

@dataclass
class TipoTest(db.Model):
    __tablename__ = 'tipo_test'
    
    id_tipo_test = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(256))
    descripcion = db.Column(db.String(256))
    
    escala_calificacion = db.relationship('EscalaCalificacion', backref='tipo_test', cascade="all,delete, delete-orphan")
    test = db.relationship('Test', backref='tipo_test', cascade="all,delete, delete-orphan")
    pregunta = db.relationship('Pregunta', backref='tipo_test', cascade="all,delete, delete-orphan")
    alternativa = db.relationship('Alternativa', backref='tipo_test', cascade="all,delete, delete-orphan")
    
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion