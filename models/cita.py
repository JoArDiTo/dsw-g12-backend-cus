from utils.db import db
from dataclasses import dataclass
from models.horario import Horario
from models.historial_clinico import HistorialClinico

@dataclass
class Cita(db.Model):
    id_cita = db.Column(db.Integer, primary_key=True)
    id_atencion = db.Column(db.Integer, db.ForeignKey('atencion.id_atencion'))
    id_historial_clinico = db.Column(db.Integer, db.ForeignKey('historial_clinico.id_historial_clinico'))
    estado = db.Column(db.Integer)
    observaciones = db.Column(db.String(1024), default="No se han definido observaciones")
    
    def __init__(self, id_atencion, id_historial_clinico, estado, observaciones):
        self.id_atencion = id_atencion
        self.id_historial_clinico = id_historial_clinico
        self.estado = estado
        self.observaciones = observaciones