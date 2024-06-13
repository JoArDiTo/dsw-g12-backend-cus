from utils.db import db
from dataclasses import dataclass
from models.tipo_test import TipoTest

@dataclass
class EscalaCalificacion(db.Model):
    __tablename__ = 'escala_calificacion'
    
    id_escala_calificacion = db.Column(db.Integer, primary_key=True)
    id_tipo_test = db.Column(db.Integer, db.ForeignKey('tipo_test.id_tipo_test'))
    descripcion = db.Column(db.String(256))
    
    rango_calificacion = db.relationship('RangoCalificacion', backref='escala_calificacion', cascade="all,delete, delete-orphan")
    
    def __init__(self, id_tipo_test, descripcion):
        self.id_tipo_test = id_tipo_test
        self.descripcion = descripcion
    