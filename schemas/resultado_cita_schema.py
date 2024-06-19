from utils.ma import ma
from models.resultado_cita import ResultadoCita
from schemas.cita_schema import CitaSchema

class ResultadoCitaSchema(ma.Schema):
    class Meta:
        model = ResultadoCita
        fields = (
            'id_resultado_cita',
            'id_cita',
            'resultado',
            'cita'
        )
        
    cita = ma.Nested(CitaSchema)
    
resultado_cita_schema = ResultadoCitaSchema()
resultados_cita_schema = ResultadoCitaSchema(many=True)