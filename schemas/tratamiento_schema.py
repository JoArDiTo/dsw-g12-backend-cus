from utils.ma import ma
from marshmallow import fields

class TratamientoSchema(ma.Schema):
    id_tratamiento = fields.Integer()
    recomendacion = fields.String()
    
semaforo_schema = TratamientoSchema()
semaforos_schema = TratamientoSchema(many=True)