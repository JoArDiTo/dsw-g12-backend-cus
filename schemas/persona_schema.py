from utils.ma import ma
from marshmallow import fields

class PersonaSchema(ma.Schema):
    documento = fields.String()
    tipo_documento = fields.String()
    nombre = fields.String()
    apellido_paterno = fields.String()
    apellido_materno = fields.String()
    telefono = fields.String()
    fecha_nacimiento = fields.Date()
    sexo = fields.String()
    
persona_schema = PersonaSchema()
personas_schema = PersonaSchema(many=True)