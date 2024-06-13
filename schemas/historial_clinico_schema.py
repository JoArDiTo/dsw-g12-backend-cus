from utils.ma import ma
from models.historial_clinico import HistorialClinico
from schemas.estudiante_schema import EstudianteSchema
from schemas.especialista_schema import EspecialistaSchema

class HistorialClinicoSchema(ma.Schema):
        class Meta:
                model = HistorialClinico
                fields = ('id_historial_clinico',
                        'cod_alumno',
                        'id_especialista',
                        'estudiante',
                        'especialista')
        
        estudiante = ma.Nested(EstudianteSchema)
        especialista = ma.Nested(EspecialistaSchema)
        
historial_clinico_schema = HistorialClinicoSchema()
historiales_clinicos_schema = HistorialClinicoSchema(many=True)