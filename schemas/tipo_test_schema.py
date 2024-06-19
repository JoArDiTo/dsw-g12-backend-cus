from utils.ma import ma
from marshmallow import fields

class TipoTestSchema(ma.Schema):
    id_tipo_test = fields.Integer()
    nombre = fields.String()
    autor = fields.String()
    descripcion = fields.String()
    
tipo_test_schema = TipoTestSchema()
tipos_test_schema = TipoTestSchema(many=True)