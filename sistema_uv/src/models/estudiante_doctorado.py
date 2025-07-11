from .alumno import Alumno

class EstudianteDoctorado(Alumno):
    def actividades(self):
        return ["Estudiar", "Hacer clases", "Investigar"]