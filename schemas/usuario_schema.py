from utils.ma import ma
from marshmallow import fields
from models.usuario import Usuario
from schemas.persona_schema import PersonaSchema

class UsuarioSchema(ma.Schema):    
    class Meta:
        model = Usuario
        fields = (
            'id_usuario',
            'documento',
            'correo',
            'password',
            'rol',
            'persona'
        )
    
    persona = ma.Nested(PersonaSchema)
    
usuario_schema = UsuarioSchema()
usuarios_schema = UsuarioSchema(many=True)