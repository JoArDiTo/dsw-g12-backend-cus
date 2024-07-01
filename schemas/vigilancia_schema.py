from utils.ma import ma
from models.vigilancia import Vigilancia
from schemas.diagnostico_schema import DiagnosticoSchema
from schemas.tratamiento_schema import TratamientoSchema

class VigilanciaSchema(ma.Schema):
    class Meta:
        model = Vigilancia
        fields = (
            'id_vigilancia',
            'id_diagnostico',
            'id_tratamiento',
            'observacion',
            'fundamentacion',
            'diagnostico',
            'tratamiento'
        )
        
    ansiedad = ma.Nested(DiagnosticoSchema)
    tratamiento = ma.Nested(TratamientoSchema)
    
vigilancia_schema = VigilanciaSchema()
vigilancias_schema = VigilanciaSchema(many=True)
        