from utils.db import db
from dataclasses import dataclass

@dataclass
class Ansiedad(db.Model):
  __tablename__ = 'ansiedad'
  
  id_ansiedad = db.Column(db.Integer, primary_key=True)
  id_especialista = db.Column(db.Integer, db.ForeignKey('especialista.id_especialista'))
  contenido = db.Column(db.String(255))
  
  vigilancia = db.relationship('Vigilancia', backref='ansiedad', cascade='all, delete-orphan')
  
  def __init__(self,id_especialista,contenido):
    self.id_especialista = id_especialista
    self.contenido = contenido