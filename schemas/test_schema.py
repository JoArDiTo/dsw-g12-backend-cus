from utils.ma import ma
from models.test import Test
from schemas.tipo_test_schema import TipoTestSchema
from schemas.paciente_schema import PacienteSchema
from schemas.clasificacion_schema import ClasificacionSchema
from schemas.vigilancia_schema import VigilanciaSchema

class TestSchema(ma.Schema):
    class Meta:
        model = Test
        fields = (
          'id_test',
          'id_tipo_test',
          'id_paciente',
          'id_clasificacion',
          'resultado',
          'fecha',
          'id_vigilancia',
          'tipo_test',
          'vigilancia',
          'clasificacion',
          'paciente'
        )
        
    tipo_test = ma.Nested(TipoTestSchema)
    paciente = ma.Nested(PacienteSchema)
    clasificacion = ma.Nested(ClasificacionSchema)
    vigilancia = ma.Nested(VigilanciaSchema)
    
test_schema = TestSchema()
tests_schema = TestSchema(many=True)