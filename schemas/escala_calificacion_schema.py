from utils.ma import ma
from models.escala_calificacion import EscalaCalificacion
from schemas.tipo_test_schema import TipoTestSchema

class EscalaCalificacionSchema(ma.Schema):
    class Meta:
        model = EscalaCalificacion
        fields = (
            'id_escala_calificacion',
            'id_tipo_test',
            'descripcion',
            'tipo_test'
        )
        
    tipo_test = ma.Nested(TipoTestSchema)
    
escala_calificacion_schema = EscalaCalificacionSchema()
escalas_calificacion_schema = EscalaCalificacionSchema(many=True)