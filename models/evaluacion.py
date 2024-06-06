from utils.db import db
from dataclasses import dataclass
from models.historial_clinico import HistorialClinico

@dataclass
class Evaluacion(db.Model):
    __tablename__ = 'evaluacion'
    
    id_evaluacion = db.Column(db.Integer, primary_key=True)
    id_historial_clinico = db.Column(db.Integer, db.ForeignKey('historial_clinico.id_historial_clinico'))
    fecha = db.Column(db.Date, default=db.func.current_date())
    estado = db.Column(db.Integer)
    tratamiento = db.Column(db.String(256))
    
    test = db.relationship('Test', backref='evaluacion', cascade="all,delete, delete-orphan")
    
    def __init__(self, id_historial_clinico, fecha, estado, tratamiento):
        self.id_historial_clinico = id_historial_clinico
        self.fecha = fecha
        self.estado = estado
        self.tratamiento = tratamiento
    
    