from .alumno import Alumno

class EstudianteMagister(Alumno):
    def actividades(self):
        return ["Estudiar", "Hacer clases"]