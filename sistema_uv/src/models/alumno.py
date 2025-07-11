from abc import ABC, abstractmethod
from typing import List
from .asignatura import Asignatura

class Alumno(ABC):
    def __init__(self, nombre: str, edad: int, rut: str, fecha_nacimiento: str):
        self.nombre = nombre
        self.edad = edad
        self.rut = rut
        self.fecha_nacimiento = fecha_nacimiento
        self.asignaturas: List[Asignatura] = []

    def agregar_asignatura(self, asignatura: Asignatura):
        self.asignaturas.append(asignatura)

    def descargar_notas(self):
        print(f"Descargando notas de {self.nombre} para asignaturas: {[a.nombre for a in self.asignaturas]}")

    @abstractmethod
    def actividades(self):
        pass