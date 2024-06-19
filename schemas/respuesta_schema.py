from utils.ma import ma
from models.respuesta import Respuesta
from schemas.test_schema import TestSchema
from schemas.pregunta_schema import PreguntaSchema
from schemas.alternativa_schema import AlternativaSchema

class RespuestaSchema(ma.Schema):
  class Meta:
    model = Respuesta
    fields = (
      'id_respuesta',
      'id_test',
      'id_pregunta',
      'id_alternativa',
      'test',
      'pregunta',
      'alternativa'
    )
    
  test = ma.Nested(TestSchema)
  alternativa = ma.Nested(AlternativaSchema)

respuesta_schema = RespuestaSchema()
respuestas_schema = RespuestaSchema(many=True)