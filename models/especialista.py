from utils.db import db
from dataclasses import dataclass
from models.usuario import Usuario

@dataclass
class Especialista(db.Model):
    __tablename__ = 'especialista'
    
    id_especialista = db.Column(db.Integer, primary_key=True)
    numero_de_colegiatura = db.Column(db.String(5))
    documento = db.Column(db.String(15), db.ForeignKey('usuario.documento'))
    
    historia_clinica = db.relationship('HistorialClinico', backref='especialista', cascade="all,delete, delete-orphan")
    horario = db.relationship('Horario', backref='especialista', cascade="all,delete, delete-orphan")
    
    def __init__(self, numero_de_colegiatura, documento):
        self.numero_de_colegiatura = numero_de_colegiatura
        self.documento = documento