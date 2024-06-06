from utils.db import db
from dataclasses import dataclass
from werkzeug.security import generate_password_hash

@dataclass
class Usuario(db.Model):
    __tablename__ = 'usuario'

    documento = db.Column(db.String(15), primary_key=True)
    tipo_documento = db.Column(db.String(15))
    nombre = db.Column(db.String(60))
    apellido_paterno = db.Column(db.String(30))
    apellido_materno = db.Column(db.String(30))
    telefono = db.Column(db.String(10))
    correo = db.Column(db.String(150))
    password = db.Column(db.String(256))
    id_tipo_rol = db.Column(db.Integer, db.ForeignKey('tipo_rol.id_tipo_rol'))
        
    estudiante = db.relationship('Estudiante', backref='persona', cascade="all,delete, delete-orphan")
    especialista = db.relationship('Especialista', backref='persona', cascade="all,delete, delete-orphan")
    
    
    def __init__(self,documento,tipo_documento,nombre,apellido_paterno,apellido_materno,telefono,correo,password,id_tipo_rol):
        self.documento = documento
        self.tipo_documento = tipo_documento
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.telefono = telefono
        self.correo = correo
        self.password = generate_password_hash(password)
        self.id_tipo_rol = id_tipo_rol
    