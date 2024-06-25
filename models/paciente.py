from models.usuario import Usuario
from dataclasses import dataclass
from utils.db import db

@dataclass
class Paciente(db.Model):
    __tablename__ = 'paciente'
    
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'))
    id_paciente = db.Column(db.Integer, primary_key=True)
    
    test = db.relationship('Test', backref='paciente', cascade='all, delete-orphan')
    cita = db.relationship('Cita', backref='paciente', cascade='all, delete-orphan')
    
    def __init__(self,id_usuario):
        self.id_usuario = id_usuario