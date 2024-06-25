from models.usuario import Usuario
from utils.db import db
from dataclasses import dataclass

@dataclass
class Especialista(db.Model):
    __tablename__ = 'especialista'
    
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'))
    id_especialista = db.Column(db.Integer, primary_key=True)
    especialidad = db.Column(db.String(60))
    licencia = db.Column(db.String(255))
    
    cita = db.relationship('Cita', backref='especialista', cascade='all, delete-orphan')
        
    def __init__(self,id_usuario,licencia,especialidad):
        self.id_usuario = id_usuario
        self.licencia = licencia
        self.especialidad = especialidad