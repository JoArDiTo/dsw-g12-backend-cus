from utils.ma import ma
from models.cita import Cita
from schemas.atencion_schema import AtencionSchema
from schemas.historial_clinico_schema import HistorialClinicoSchema

class CitaSchema(ma.Schema):
    class Meta:
        model = Cita
        fields = (
            'id_cita',
            'id_atencion',
            'id_historial_clinico',
            'estado',
            'observaciones',
            'atencion',
            'historial_clinico'
        )
        
    atencion = ma.Nested(AtencionSchema)
    historial_clinico = ma.Nested(HistorialClinicoSchema)
    
cita_schema = CitaSchema()
citas_schema = CitaSchema(many=True)