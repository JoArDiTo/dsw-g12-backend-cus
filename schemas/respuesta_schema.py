from schemas.alternativa_schema import AlternativaSchema
from schemas.pregunta_schema import PreguntaSchema
from schemas.test_schema import TestSchema
from models.respuesta import Respuesta
from utils.ma import ma


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
  pregunta = ma.Nested(PreguntaSchema)
  alternativa = ma.Nested(AlternativaSchema)

respuesta_schema = RespuestaSchema()
respuestas_schema = RespuestaSchema(many=True)