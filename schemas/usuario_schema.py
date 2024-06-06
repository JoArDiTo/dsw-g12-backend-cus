from utils.ma import ma
from marshmallow import fields
from models.usuario import Usuario
from schemas.tipo_rol_schema import TipoRolSchema

class UsuarioSchema(ma.Schema):    
    class Meta:
        model = Usuario
        fields = (
            'documento',
            'tipo_documento',
            'id_tipo_rol',
            'nombre',
            'apellido_paterno',
            'apellido_materno',
            'telefono',
            'correo',
            'password',
            'tipo_rol'
        )
    
    tipo_rol = ma.Nested(TipoRolSchema)
    
usuario_schema = UsuarioSchema()
usuarios_schema = UsuarioSchema(many=True)