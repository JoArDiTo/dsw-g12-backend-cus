from utils.ma import ma
from models.especialista import Especialista
from schemas.usuario_schema import UsuarioSchema

class EspecialistaSchema(ma.Schema):
    class Meta:
        model = Especialista
        fields = (
            "id_especialista",
            "documento",
            "numero_de_colegiatura",
            "usuario")

    usuario = ma.Nested(UsuarioSchema)

especialista_schema = EspecialistaSchema()
especialistas_schema = EspecialistaSchema(many=True)