from utils.ma import ma
from models.vigilancia import Vigilancia
from schemas.ansiedad_schema import AnsiedadSchema
from schemas.tratamiento_schema import TratamientoSchema

class VigilanciaSchema(ma.Schema):
    class Meta:
        model = Vigilancia
        fields = (
            'id_vigilancia',
            'id_ansiedad',
            'id_tratamiento',
            'ansiedad',
            'tratamiento'
        )
        
    ansiedad = ma.Nested(AnsiedadSchema)
    tratamiento = ma.Nested(TratamientoSchema)
    
vigilancia_schema = VigilanciaSchema()
vigilancias_schema = VigilanciaSchema(many=True)
        