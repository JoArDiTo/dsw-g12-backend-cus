from utils.ma import ma
from marshmallow import fields

class UbigeoSchema(ma.Schema):
    id_ubigeo = fields.String()
    departamento = fields.String()
    provincia = fields.String()
    distrito = fields.String()
    latitud = fields.Float()
    longitud = fields.Float()
    
ubigeo_schema = UbigeoSchema()
ubigeos_schema = UbigeoSchema(many=True)
