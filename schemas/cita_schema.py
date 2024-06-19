from utils.ma import ma
from models.cita import Cita
from schemas.paciente_schema import PacienteSchema
from schemas.especialista_schema import EspecialistaSchema

class CitaSchema(ma.Schema):
    class Meta:
        model = Cita
        fields = (
            'id_cita',
            'id_paciente',
            'id_especialista',
            'motivo',
            'detalle',
            'estado',
            'paciente',
            'especialista'
        )
        
    paciente = ma.Nested(PacienteSchema)
    especialista = ma.Nested(EspecialistaSchema)
        
cita_schema = CitaSchema()
citas_schema = CitaSchema(many=True)