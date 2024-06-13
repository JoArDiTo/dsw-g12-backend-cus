from utils.ma import ma
from models.alternativa import Alternativa
from schemas.tipo_rol_schema import TipoRolSchema

class AlternativaSchema(ma.Schema):
    class Meta:
        model = Alternativa
        fields = (
        'id_alternativa',
        'id_tipo_test',
        'texto',
        'puntaje',
        'pregunta'
        )
        
    pregunta = ma.Nested(TipoRolSchema)
    
alternativa_schema = AlternativaSchema()
alternativas_schema = AlternativaSchema(many=True)