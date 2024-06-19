from utils.ma import ma
from models.pregunta import Pregunta
from schemas.tipo_test_schema import TipoTestSchema

class PreguntaSchema(ma.Schema):
  class Meta:
    model = Pregunta
    fields = (
      'id_pregunta',
      'id_tipo_test',
      'contenido',
      'invertido',
      'tipo_test'
    )
    
  tipo_test = ma.Nested(TipoTestSchema)
  
pregunta_schema = PreguntaSchema()
preguntas_schema = PreguntaSchema(many=True)