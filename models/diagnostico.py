from utils.db import db
from dataclasses import dataclass
from models.tratamiento import Tratamiento
from models.paciente import Paciente
from models.especialista import Especialista

@dataclass
class Diagnostico(db.Model):
    __tablename__ = 'diagnostico'
    
    id_diagnostico = db.Column(db.Integer, primary_key=True)
    id_paciente = db.Column(db.Integer, db.ForeignKey('paciente.id_paciente'))
    id_especialista = db.Column(db.Integer, db.ForeignKey('especialista.id_especialista'))
    id_tratamiento = db.Column(db.Integer, db.ForeignKey('tratamiento.id_tratamiento'))
    
    def __init__(self,id_paciente,id_especialista,id_tratamiento):
        self.id_paciente = id_paciente
        self.id_especialista = id_especialista
        self.id_tratamiento = id_tratamiento