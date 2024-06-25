from models.ubigeo import Ubigeo
from dataclasses import dataclass
from utils.db import db

@dataclass
class Persona(db.Model):
    __tablename__ = 'persona'
    
    documento = db.Column(db.String(15), primary_key=True)
    fecha_nacimiento = db.Column(db.Date)
    id_ubigeo = db.Column(db.String(6), db.ForeignKey('ubigeo.id_ubigeo'))
    tipo_documento = db.Column(db.String(9)) # DNI, CE, PASAPORTE
    telefono = db.Column(db.String(15))
    apellido_paterno = db.Column(db.String(50))
    nombre = db.Column(db.String(50))
    apellido_materno = db.Column(db.String(50))
    sexo = db.Column(db.String(1)) # M, F o X
    
    usuario = db.relationship('Usuario', backref='persona', cascade="all,delete, delete-orphan", uselist=True, lazy=True)
    
    def __init__(self,documento,tipo_documento,nombre,apellido_paterno,apellido_materno,telefono,fecha_nacimiento,sexo, id_ubigeo):
        self.documento = documento
        self.tipo_documento = tipo_documento
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.telefono = telefono
        self.fecha_nacimiento = fecha_nacimiento
        self.sexo = sexo
        self.id_ubigeo = id_ubigeo