from utils.db import db
from dataclasses import dataclass

@dataclass
class Tratamiento(db.Model):
    __tablename__ = 'tratamiento'
    
    id_tratamiento = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(255))
    fecha = db.Column(db.Date)
    
    diagnostico = db.relationship('Diagnostico', backref='tratamiento', cascade='all, delete-orphan')
    
    def __init__(self,descripcion,fecha):
        self.descripcion = descripcion
        self.fecha = fecha