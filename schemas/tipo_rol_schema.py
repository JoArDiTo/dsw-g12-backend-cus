from utils.ma import ma
from marshmallow import fields

class TipoRolSchema(ma.Schema):
    id_tipo_rol = fields.Integer()
    descripcion = fields.String()
    
tipo_roles_schema = TipoRolSchema()
tipos_roles_schema = TipoRolSchema(many=True)