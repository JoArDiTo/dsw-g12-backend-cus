from utils.db import db
from dataclasses import dataclass
from models.usuario import Usuario

@dataclass
class Estudiante(db.Model):
    __tablename__ = 'estudiante'
    
    cod_alumno = db.Column(db.Integer, primary_key=True)
    anio_ingreso = db.Column(db.Integer)
    ciclo_estudio = db.Column(db.Integer)
    base = db.Column(db.Integer)
    facultad = db.Column(db.String(100))
    carrera = db.Column(db.String(100))
    documento = db.Column(db.String(15), db.ForeignKey('usuario.documento'))    

    historial_clinico = db.relationship('HistorialClinico', backref='estudiante', cascade="all,delete, delete-orphan")
    
    def __init__(self, cod_alumno, anio_ingreso, ciclo_estudio, base, facultad, carrera, documento):
        self.cod_alumno = cod_alumno
        self.anio_ingreso = anio_ingreso
        self.ciclo_estudio = ciclo_estudio
        self.base = base
        self.facultad = facultad
        self.carrera = carrera
        self.documento = documento