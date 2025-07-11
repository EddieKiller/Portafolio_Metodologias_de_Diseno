from .alumno import Alumno


class EstudianteNoAyudante(Alumno):
    def actividades(self):
        return ["Estudiar"]