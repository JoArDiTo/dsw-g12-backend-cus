from utils.ma import ma
from schemas.usuario_schema import UsuarioSchema
from models.especialista import Especialista

class EspecialistaSchema(ma.Schema):
    class Meta:
        model = Especialista
        fields = (
            'id_especialista',
            'id_usuario',
            'licencia',
            'especialidad',
            'usuario'
        )

    usuario = ma.Nested(UsuarioSchema)

especialista_schema = EspecialistaSchema()
especialistas_schema = EspecialistaSchema(many=True)