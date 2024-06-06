from utils.db import db
from dataclasses import dataclass
from models.evaluacion import Evaluacion
from models.tipo_test import TipoTest

@dataclass
class Test(db.Model):
    __tablename__ = 'test'
    
    id_test = db.Column(db.Integer, primary_key=True)
    id_evaluacion = db.Column(db.Integer, db.ForeignKey('evaluacion.id_evaluacion'))
    id_tipo_test = db.Column(db.Integer, db.ForeignKey('tipo_test.id_tipo_test'))
    puntaje_total = db.Column(db.Integer, default=0)
    diagnostico = db.Column(db.String(30))
    
    respuesta = db.relationship('Respuesta', backref='test', cascade="all,delete, delete-orphan")
    
    def __init__(self, id_evaluacion, id_tipo_test, puntaje_total, diagnostico):
        self.id_evaluacion = id_evaluacion
        self.id_tipo_test = id_tipo_test
        self.puntaje_total = puntaje_total
        self.diagnostico = diagnostico