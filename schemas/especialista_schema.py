from models.especialista import Especialista
from schemas.usuario_schema import UsuarioSchema
from utils.ma import ma

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