from utils.db import db
from dataclasses import dataclass
from models.test import Test
import datetime

@dataclass
class Vigilancia(db.Model):
    __tablename__ = 'vigilancia'
    
    id_vigilancia = db.Column(db.Integer, primary_key=True)
    id_ansiedad = db.Column(db.Integer, db.ForeignKey('ansiedad.id_ansiedad'))
    id_tratamiento = db.Column(db.Integer, db.ForeignKey('tratamiento.id_tratamiento'))
    
    test = db.relationship('Test', backref='vigilancia', cascade='all, delete-orphan')
    
    def __init__(self, id_ansiedad, id_tratamiento):
        self.id_ansiedad = id_ansiedad
        self.id_tratamiento = id_tratamiento