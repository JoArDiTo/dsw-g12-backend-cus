from utils.ma import ma
from marshmallow import fields
from models.estudiante import Estudiante
from schemas.usuario_schema import UsuarioSchema

class EstudianteSchema(ma.Schema):
    class Meta:
        model = Estudiante
        fields = ('cod_alumno',
                'documento',
                'anio_ingreso',
                'ciclo_estudio',
                'base',
                'facultad',
                'carrera',
                'usuario'
        )
        
    usuario = ma.Nested(UsuarioSchema)
    
estudiante_schema = EstudianteSchema()
estudiantes_schema = EstudianteSchema(many=True)