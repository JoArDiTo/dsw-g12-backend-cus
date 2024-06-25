from schemas.ubigeo_schema import UbigeoSchema
from utils.ma import ma
from models.persona import Persona

class PersonaSchema(ma.Schema):
    class Meta:
        model = Persona
        fields = (
            'documento',
            'id_ubigeo',
            'fecha_nacimiento',
            'nombre',
            'apellido_paterno',
            'sexo',
            'apellido_materno',
            'tipo_documento',
            'telefono',
            'ubigeo'
        )
        
    ubigeo = ma.Nested(UbigeoSchema)
    
persona_schema = PersonaSchema()
personas_schema = PersonaSchema(many=True)