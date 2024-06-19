from utils.ma import ma
from marshmallow import fields
from models.paciente import Paciente
from schemas.usuario_schema import UsuarioSchema

class PacienteSchema(ma.Schema):
    class Meta:
        model = Paciente
        fields = (
            'id_paciente',
            'id_usuario',
            'usuario'
        )
        
    usuario = ma.Nested(UsuarioSchema)
    
paciente_schema = PacienteSchema()
pacientes_schema = PacienteSchema(many=True)