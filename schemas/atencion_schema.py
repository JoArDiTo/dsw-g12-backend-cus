from utils.ma import ma
from models.atencion import Atencion
from schemas.horario_schema import HorarioSchema

class AtencionSchema(ma.Schema):
    class Meta:
        model = Atencion
        fields = (
            "id_atencion",
            "id_horario",
            "fecha",
            "hora_inicio",
            "hora_fin",
            "reservado",
            "horario"
        )

    horario = ma.Nested(HorarioSchema)
    
atencion_schema = AtencionSchema()
atenciones_schema = AtencionSchema(many=True)