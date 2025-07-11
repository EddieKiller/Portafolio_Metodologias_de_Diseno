from typing import Dict, Optional
from src.models.alumno import Alumno
from src.models.asignatura import Asignatura


class DB:
    alumnos: Dict[str, Alumno] = {}
    asignaturas: Dict[str, Asignatura] = {}

    @classmethod
    def insertar_alumno(cls, alumno: Alumno):
        cls.alumnos[alumno.rut] = alumno
        print(f"Alumno insertado: {alumno.nombre} ({alumno.rut})")

    @classmethod
    def obtener_alumno(cls, rut: str) -> Optional[Alumno]:
        return cls.alumnos.get(rut)

    @classmethod
    def modificar_alumno(cls, rut: str, **kwargs):
        alumno = cls.alumnos.get(rut)
        if alumno:
            for key, value in kwargs.items():
                if hasattr(alumno, key):
                    setattr(alumno, key, value)
            print(f"Alumno modificado: {alumno.nombre} ({alumno.rut})")

    @classmethod
    def eliminar_alumno(cls, rut: str):
        if rut in cls.alumnos:
            del cls.alumnos[rut]
            print(f"Alumno eliminado: {rut}")

    @classmethod
    def insertar_asignatura(cls, asignatura: Asignatura):
        cls.asignaturas[asignatura.codigo] = asignatura
        print(f"Asignatura insertada: {asignatura.nombre} ({asignatura.codigo})")

    @classmethod
    def obtener_asignatura(cls, codigo: str) -> Optional[Asignatura]:
        return cls.asignaturas.get(codigo)

    @classmethod
    def modificar_asignatura(cls, codigo: str, **kwargs):
        asignatura = cls.asignaturas.get(codigo)
        if asignatura:
            for key, value in kwargs.items():
                if hasattr(asignatura, key):
                    setattr(asignatura, key, value)
            print(f"Asignatura modificada: {asignatura.nombre} ({asignatura.codigo})")

    @classmethod
    def eliminar_asignatura(cls, codigo: str):
        if codigo in cls.asignaturas:
            del cls.asignaturas[codigo]
            print(f"Asignatura eliminada: {codigo}")