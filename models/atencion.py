from utils.db import db
from dataclasses import dataclass
from models.horario import Horario

@dataclass
class Atencion(db.Model):
    __tablename__ = 'atencion'
    
    id_atencion = db.Column(db.Integer, primary_key=True)
    id_horario = db.Column(db.Integer, db.ForeignKey('horario.id_horario'))
    fecha = db.Column(db.Date)
    hora_inicio = db.Column(db.Date)
    hora_fin = db.Column(db.Date)
    reservado = db.Column(db.String(1))

    cita = db.relationship('Cita', backref='atencion', cascade="all,delete, delete-orphan")
    
    def __init__(self, id_horario, id_historial_clinico, fecha, hora_inicio, hora_fin, reservado):
        self.id_horario = id_horario
        self.id_historial_clinico = id_historial_clinico
        self.fecha = fecha
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.reservado = reservado