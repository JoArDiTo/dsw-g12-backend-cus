from utils.ma import ma
from models.horario import Horario
from schemas.especialista_schema import EspecialistaSchema

class HorarioSchema(ma.Schema):
    class Meta:
        model = Horario
        fields = (
            "id_horario",
            "id_especialista",
            "estado",
            "especialista"
        )

    especialista = ma.Nested(EspecialistaSchema)
    
horario_schema = HorarioSchema()
horarios_schema = HorarioSchema(many=True)