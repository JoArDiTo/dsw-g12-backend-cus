from utils.db import db
from dataclasses import dataclass
from models.tipo_test import TipoTest
from models.semaforo import Semaforo

@dataclass
class Clasificacion(db.Model):
    __tablename__ = 'clasificacion'
    
    id_clasificacion = db.Column(db.Integer, primary_key=True)
    id_tipo_test = db.Column(db.Integer, db.ForeignKey('tipo_test.id_tipo_test'))
    minimo = db.Column(db.Integer)
    maximo = db.Column(db.Integer)
    interpretacion = db.Column(db.String(255))
    id_semaforo = db.Column(db.Integer, db.ForeignKey('semaforo.id_semaforo'))
    
    def __init__(self,id_tipo_test,minimo,maximo,interpretacion, id_semaforo):
        self.id_tipo_test = id_tipo_test
        self.minimo = minimo
        self.maximo = maximo
        self.interpretacion = interpretacion
        self.id_semaforo = id_semaforo
