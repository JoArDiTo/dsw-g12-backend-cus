from utils.ma import ma
from models.evaluacion import Evaluacion
from schemas.historial_clinico_schema import HistorialClinicoSchema

class EvaluacionSchema(ma.Schema):
    class Meta:
        model = Evaluacion
        fields = ('id_evaluacion',
                'id_historial_clinico',
                'fecha',
                'estado',
                'tratamiento',
                'historial_clinico')
        
    historial_clinico = ma.Nested(HistorialClinicoSchema)
    
evaluacion_schema = EvaluacionSchema()
evaluaciones_schema = EvaluacionSchema(many=True)