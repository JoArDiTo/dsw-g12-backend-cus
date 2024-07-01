from utils.ma import ma
from marshmallow import fields

class DiagnosticoSchema(ma.Schema):
    id_diagnostico = fields.Integer()
    descripcion = fields.String()
    fundamentacion = fields.String()
        
    
diagnostico_schema = DiagnosticoSchema()
diagnosticos_schema = DiagnosticoSchema(many=True)