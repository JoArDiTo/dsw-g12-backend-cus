from utils.db import db
from dataclasses import dataclass

@dataclass
class Diagnostico(db.Model):
  __tablename__ = 'diagnostico'
  
  id_ansiedad = db.Column(db.Integer, primary_key=True)
  descripcion = db.Column(db.String(60))
  fundamentacion = db.Column(db.String(255))
  
  vigilancia = db.relationship('Vigilancia', backref='diagnostico', cascade='all, delete-orphan')
  
  def __init__(self,id_especialista,descripcion, fundamentacion):
    self.id_especialista = id_especialista
    self.descripcion = descripcion
    self.fundamentacion = fundamentacion