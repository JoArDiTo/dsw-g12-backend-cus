from utils.db import db
from dataclasses import dataclass
from models.usuario import Usuario

@dataclass
class Paciente(db.Model):
    __tablename__ = 'paciente'
    
    id_paciente = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'))
    
    cita = db.relationship('Cita', backref='paciente', cascade='all, delete-orphan')
    test = db.relationship('Test', backref='paciente', cascade='all, delete-orphan')
    
    def __init__(self,id_usuario):
        self.id_usuario = id_usuario