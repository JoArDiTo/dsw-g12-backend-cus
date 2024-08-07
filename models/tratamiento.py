from utils.db import db
from dataclasses import dataclass

@dataclass
class Tratamiento(db.Model):
  __tablename__ = 'tratamiento'
  
  id_tratamiento = db.Column(db.Integer, primary_key=True)
  descripcion = db.Column(db.String(80))
  fundamentacion = db.Column(db.String(255))
  
  vigilancia = db.relationship('Vigilancia', backref='tratamiento', cascade='all, delete-orphan')
  
  def __init__(self, descripcion, fundamentacion):
    self.descripcion = descripcion
    self.fundamentacion = fundamentacion