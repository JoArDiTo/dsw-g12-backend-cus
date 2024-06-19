from utils.db import db
from dataclasses import dataclass

@dataclass
class TipoTest(db.Model):
    __tablename__ = 'tipo_test'
    
    id_tipo_test = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255))
    autor = db.Column(db.String(200))
    descripcion = db.Column(db.String(255))
    
    pregunta = db.relationship('Pregunta', backref='tipo_test', cascade='all, delete-orphan')
    alternativa = db.relationship('Alternativa', backref='tipo_test', cascade='all, delete-orphan')
    clasificacion = db.relationship('Clasificacion', backref='tipo_test', cascade='all, delete-orphan')
    test = db.relationship('Test', backref='tipo_test', cascade='all, delete-orphan')
    
    def __init__(self,nombre,autor,descripcion):
        self.nombre = nombre
        self.autor = autor
        self.descripcion = descripcion