from utils.db import db
from dataclasses import dataclass

@dataclass
class Tratamiento(db.Model):
  __tablename__ = 'tratamiento'
  
  id_tratamiento = db.Column(db.Integer, primary_key=True)
  recomendacion = db.Column(db.String(255))
  
  vigilancia = db.relationship('Vigilancia', backref='tratamiento', cascade='all, delete-orphan')
  
  def __init__(self,recomendacion):
    self.recomendacion = recomendacion