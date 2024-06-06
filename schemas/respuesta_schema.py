from utils.ma import ma
from models.respuesta import Respuesta
from schemas.test_schema import TestSchema

class RespuestaSchema(ma.Schema):
  class Meta:
    model = Respuesta
    fields = (
      'id_respuesta',
      'id_test',
      'pregunta',
      'respuesta',
      'puntaje',
      'test'
    )
    
  test = ma.Nested(TestSchema)

respuesta_schema = RespuestaSchema()
respuestas_schema = RespuestaSchema(many=True)