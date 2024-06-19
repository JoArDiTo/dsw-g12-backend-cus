from utils.ma import ma
from models.clasificacion import Clasificacion
from schemas.tipo_test_schema import TipoTestSchema
from schemas.semaforo_schema import SemaforoSchema

class ClasificacionSchema(ma.Schema):
    class Meta:
        model = Clasificacion
        fields = (
            'id_clasificacion',
            'id_tipo_test',
            'minimo',
            'maximo',
            'interpretacion',
            'tipo_test',
            'semaforo'
        )
        
    tipo_test = ma.Nested(TipoTestSchema)
    semaforo = ma.Nested(SemaforoSchema)

clasificacion_schema = ClasificacionSchema()
clasificaciones_schema = ClasificacionSchema(many=True)