from utils.db import db
from dataclasses import dataclass
from werkzeug.security import generate_password_hash
from models.persona import Persona

@dataclass
class Usuario(db.Model):
    __tablename__ = 'usuario'

    id_usuario = db.Column(db.Integer, primary_key=True)
    documento = db.Column(db.String(15), db.ForeignKey('persona.documento'))
    correo = db.Column(db.String(60))
    password = db.Column(db.String(255))
    
    paciente = db.relationship('Paciente', backref='usuario', cascade="all,delete, delete-orphan")
    especialista = db.relationship('Especialista', backref='usuario', cascade="all,delete, delete-orphan")
    
    def __init__(self,documento,correo,password):
        self.documento = documento
        self.correo = correo
        self.password = generate_password_hash(password)