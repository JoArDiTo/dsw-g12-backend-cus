from utils.db import db
from dataclasses import dataclass
from models.paciente import Paciente
from models.especialista import Especialista

@dataclass
class Cita(db.Model):
    __tablename__ = 'cita'
    
    id_cita = db.Column(db.Integer, primary_key=True)
    id_paciente = db.Column(db.Integer, db.ForeignKey('paciente.id_paciente'))
    id_especialista = db.Column(db.Integer, db.ForeignKey('especialista.id_especialista'))
    motivo = db.Column(db.String(255))
    detalle = db.Column(db.String(255))
    estado = db.Column(db.String(12)) # En espera, cancelada, realizada
    
    resultado_cita = db.relationship('ResultadoCita', backref='cita', cascade='all, delete-orphan')  
    
    def __init__(self,id_paciente,id_especialista,motivo,detalle,estado):
        self.id_paciente = id_paciente
        self.id_especialista = id_especialista
        self.motivo = motivo
        self.detalle = detalle
        self.estado = estado