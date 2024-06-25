from utils.ma import ma
from models.ansiedad import Ansiedad
from schemas.especialista_schema import EspecialistaSchema

class AnsiedadSchema(ma.Schema):
    class Meta:
        model = Ansiedad
        fields = (
            'id_ansiedad',
            'id_especialista',
            'contenido'
            'especialista'
        )
        
    especialista = ma.Nested(EspecialistaSchema)
    
ansiedad_schema = AnsiedadSchema()
ansiedades_schema = AnsiedadSchema(many=True)