from utils.db import db
from dataclasses import dataclass
from models.especialista import Especialista

@dataclass
class Horario(db.Model):
    __tablename__ = 'horario'
    
    id_horario = db.Column(db.Integer, primary_key=True)
    id_especialista = db.Column(db.Integer, db.ForeignKey('especialista.id_especialista'))
    estado = db.Column(db.Boolean)
    
    atencion = db.relationship('Atencion', backref='horario', cascade="all,delete, delete-orphan")
    
    def __init__(self, id_especialista, estado):
        self.id_especialista = id_especialista
        self.estado = estado