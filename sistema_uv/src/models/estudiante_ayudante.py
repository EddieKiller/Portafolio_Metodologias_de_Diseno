from .alumno import Alumno

class EstudianteAyudante(Alumno):
    def actividades(self):
        return ["Estudiar", "Ayudantía"]