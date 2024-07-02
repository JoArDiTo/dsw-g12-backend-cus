from utils.db import db
from dataclasses import dataclass
from models.test import Test
import datetime

@dataclass
class Vigilancia(db.Model):
    __tablename__ = 'vigilancia'
    
    id_vigilancia = db.Column(db.Integer, primary_key=True)
    id_diagnostico = db.Column(db.Integer, db.ForeignKey('diagnostico.id_diagnostico'))
    id_tratamiento = db.Column(db.Integer, db.ForeignKey('tratamiento.id_tratamiento'))
    observacion = db.Column(db.String(255))
    fundamentacion = db.Column(db.String(255))
    
    test = db.relationship('Test', backref='vigilancia', cascade='all, delete-orphan')
    
    def __init__(self, id_diagnostico, id_tratamiento, observacion, fundamentacion):
        self.id_diagnostico = id_diagnostico
        self.id_tratamiento = id_tratamiento
        self.observacion = observacion
        self.fundamentacion = fundamentacion