from utils.ma import ma
from models.diagnostico import Diagnostico
from schemas.tratamiento_schema import TratamientoSchema
from schemas.paciente_schema import PacienteSchema
from schemas.especialista_schema import EspecialistaSchema

class DiagnosticoSchema(ma.Schema):
    class Meta:
        model = Diagnostico
        fields = (
            'id_diagnostico',
            'id_paciente',
            'id_especialista',
            'id_tratamiento',
            'paciente',
            'especialista',
            'tratamiento'
        )
        
    paciente = ma.Nested(PacienteSchema)
    especialista = ma.Nested(EspecialistaSchema)
    tratamiento = ma.Nested(TratamientoSchema)
    
diagnostico_schema = DiagnosticoSchema()
diagnosticos_schema = DiagnosticoSchema(many=True)