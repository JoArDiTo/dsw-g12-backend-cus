from utils.db import db
from dataclasses import dataclass

@dataclass
class TipoRol(db.Model):
    __tablename__ = 'tipo_rol'
    
    id_tipo_rol = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(15))
    
    usuario = db.relationship('Usuario', backref='tipo_rol', cascade="all,delete, delete-orphan")
    
    def __init__(self, descripcion):
        self.descripcion = descripcion
