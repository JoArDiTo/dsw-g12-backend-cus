from utils.db import db
from dataclasses import dataclass

@dataclass
class Diagnostico(db.Model):
  __tablename__ = 'diagnostico'
  
  id_diagnostico = db.Column(db.Integer, primary_key=True)
  descripcion = db.Column(db.String(60))
  fundamentacion = db.Column(db.String(255))
  
  vigilancia = db.relationship('Vigilancia', backref='diagnostico', cascade='all, delete-orphan')
  
  def __init__(self,descripcion, fundamentacion):
    self.descripcion = descripcion
    self.fundamentacion = fundamentacion