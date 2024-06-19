from utils.db import db
from dataclasses import dataclass

@dataclass
class Semaforo(db.Model):
    __tablename__ = 'semaforo'
    
    id_semaforo = db.Column(db.Integer, primary_key=True)
    color = db.Column(db.String(6))
    
    clasificacion = db.relationship('Clasificacion', backref='semaforo', cascade='all, delete-orphan')
    
    def __init__(self,color):
        self.color = color