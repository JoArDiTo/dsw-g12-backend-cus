from utils.ma import ma
from models.test import Test
from schemas.tipo_test_schema import TipoTestSchema
from schemas.evaluacion_schema import EvaluacionSchema

class TestSchema(ma.Schema):
    class Meta:
        model = Test
        fields = (
          'id_test',
          'id_evaluacion',
          'id_tipo_test',
          'puntaje_total',
          'diagnostico',
          'evaluacion',
          'tipo_test'
        )
        
    evaluacion = ma.Nested(EvaluacionSchema)
    tipo_test = ma.Nested(TipoTestSchema)
    
test_schema = TestSchema()
tests_schema = TestSchema(many=True)