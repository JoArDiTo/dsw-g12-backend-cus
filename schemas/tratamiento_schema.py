from utils.ma import ma
from marshmallow import fields

class TratamientoSchema(ma.Schema):
    id_tratamiento = fields.Integer()
    descripcion = fields.String()
    fundamentacion = fields.String()
    
tratamiento_schema = TratamientoSchema()
tratamientos_schema = TratamientoSchema(many=True)