from utils.ma import ma
from models.test import Test
from schemas.tipo_test_schema import TipoTestSchema
from schemas.paciente_schema import PacienteSchema

class TestSchema(ma.Schema):
    class Meta:
        model = Test
        fields = (
          'id_test',
          'id_tipo_test',
          'id_paciente',
          'resultado',
          'interpretacion',
          'fecha',
          'color',
          'ansiedad_consignada',
          'observaciones',
          'consignado'
          'tipo_test',
          'paciente'
        )
        
    tipo_test = ma.Nested(TipoTestSchema)
    paciente = ma.Nested(PacienteSchema)
    
test_schema = TestSchema()
tests_schema = TestSchema(many=True)