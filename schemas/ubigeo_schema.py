from utils.ma import ma
from marshmallow import fields

class UbigeoSchema(ma.Schema):
    id_ubigeo = fields.Integer()
    departamento = fields.String()
    provincia = fields.String()
    distrito = fields.String()
    
ubigeo_schema = UbigeoSchema()
ubigeos_schema = UbigeoSchema(many=True)
