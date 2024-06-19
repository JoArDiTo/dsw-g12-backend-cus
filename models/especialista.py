from utils.db import db
from dataclasses import dataclass
from models.usuario import Usuario

@dataclass
class Especialista(db.Model):
    __tablename__ = 'especialista'
    
    id_especialista = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'))
    licencia = db.Column(db.String(255))
    especialidad = db.Column(db.String(60))
    
    cita = db.relationship('Cita', backref='especialista', cascade='all, delete-orphan')
        
    def __init__(self,id_usuario,licencia,especialidad):
        self.id_usuario = id_usuario
        self.licencia = licencia
        self.especialidad = especialidad