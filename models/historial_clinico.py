from utils.db import db
from dataclasses import dataclass
from models.estudiante import Estudiante
from models.especialista import Especialista

@dataclass
class HistorialClinico(db.Model):
    __tablename__ = 'historial_clinico'
    id_historial_clinico = db.Column(db.Integer, primary_key=True)
    cod_alumno = db.Column(db.Integer, db.ForeignKey('estudiante.cod_alumno'))
    id_especialista = db.Column(db.Integer, db.ForeignKey('especialista.id_especialista'))
    
    evaluaciones = db.relationship('Evaluacion', backref='historial_clinico', cascade="all,delete, delete-orphan")
    cita = db.relationship('Cita', backref='historial_clinico', cascade="all,delete, delete-orphan")
    

    def __init__(self, cod_alumno, id_especialista):
        self.cod_alumno = cod_alumno
        self.id_especialista = id_especialista
