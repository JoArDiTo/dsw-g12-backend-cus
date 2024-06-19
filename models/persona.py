from utils.db import db
from dataclasses import dataclass

@dataclass
class Persona(db.Model):
    __tablename__ = 'persona'
    
    documento = db.Column(db.String(15), primary_key=True)
    tipo_documento = db.Column(db.String(20))
    nombre = db.Column(db.String(50))
    apellido_paterno = db.Column(db.String(50))
    apellido_materno = db.Column(db.String(50))
    telefono = db.Column(db.String(15))
    fecha_nacimiento = db.Column(db.Date)
    sexo = db.Column(db.String(1)) # M, F o X
    
    usuario = db.relationship('Usuario', backref='persona', cascade="all,delete, delete-orphan", uselist=True, lazy=True)
    
    def __init__(self,documento,tipo_documento,nombre,apellido_paterno,apellido_materno,telefono,fecha_nacimiento,sexo):
        self.documento = documento
        self.tipo_documento = tipo_documento
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.telefono = telefono
        self.fecha_nacimiento = fecha_nacimiento
        self.sexo = sexo