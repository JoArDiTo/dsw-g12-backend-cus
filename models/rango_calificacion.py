from utils.db import db
from dataclasses import dataclass
from models.escala_calificacion import EscalaCalificacion

@dataclass
class RangoCalificacion(db.Model):
    __tablename__ = 'rango_calificacion'
    
    id_rango_calificacion = db.Column(db.Integer, primary_key=True)
    id_escala_calificacion = db.Column(db.Integer, db.ForeignKey('escala_calificacion.id_escala_calificacion'))
    puntaje_min = db.Column(db.Integer)
    puntaje_max = db.Column(db.Integer)
    interpretacion = db.Column(db.String(100))
    
    def __init__(self, id_escala_calificacion, puntaje_min, puntaje_max, interpretacion):
        self.id_escala_calificacion = id_escala_calificacion
        self.puntaje_min = puntaje_min
        self.puntaje_max = puntaje_max
        self.interpretacion = interpretacion
