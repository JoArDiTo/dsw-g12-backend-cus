from utils.ma import ma
from models.persona import Persona
from schemas.ubigeo_schema import UbigeoSchema

class PersonaSchema(ma.Schema):
    class Meta:
        model = Persona
        fields = (
            'documento',
            'id_ubigeo',
            'nombres',
            'apellidos',
            'fecha_nacimiento',
            'sexo',
            'telefono',
            'correo',
            'direccion',
            'ubigeo'
        )
        
    ubigeo = ma.Nested(UbigeoSchema)
    
persona_schema = PersonaSchema()
personas_schema = PersonaSchema(many=True)