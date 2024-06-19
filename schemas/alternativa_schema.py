from utils.ma import ma
from models.alternativa import Alternativa
from schemas.tipo_test_schema import TipoTestSchema

class AlternativaSchema(ma.Schema):
    class Meta:
        model = Alternativa
        fields = (
        'id_alternativa',
        'id_tipo_test',
        'contenido',
        'puntaje',
        'tipo_test'
        )
        
    tipo_test = ma.Nested(TipoTestSchema)
    
alternativa_schema = AlternativaSchema()
alternativas_schema = AlternativaSchema(many=True)