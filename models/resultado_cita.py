from utils.db import db
from dataclasses import dataclass
from models.cita import Cita

@dataclass
class ResultadoCita(db.Model):
    __tablename__ = 'resultado_cita'
    
    id_resultado_cita = db.Column(db.Integer, primary_key=True)
    id_cita = db.Column(db.Integer, db.ForeignKey('cita.id_cita'))
    observacion = db.Column(db.String(255))
    tratamiento = db.Column(db.String(255))
    
    def __init__(self,id_cita,observacion,tratamiento):
        self.id_cita = id_cita
        self.observacion = observacion
        self.tratamiento = tratamiento