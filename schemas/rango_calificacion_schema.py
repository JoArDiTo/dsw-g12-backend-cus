from utils.ma import ma
from models.rango_calificacion import RangoCalificacion
from schemas.escala_calificacion_schema import EscalaCalificacionSchema

class RangoCalificacionSchema(ma.Schema):
    class Meta:
        model = RangoCalificacion
        fields = (
            'id_rango_calificacion',
            'id_escala_calificacion',
            'puntaje_min',
            'puntaje_max',
            'interpretacion',	
            'escala_calificacion'
        )
        
    escala_calificacion = ma.Nested(EscalaCalificacionSchema)

rango_calificacion_schema = RangoCalificacionSchema()
rangos_calificacion_schema = RangoCalificacionSchema(many=True)