# File: sistema_uv/src/main.py

from models.asignatura import Asignatura
from models.estudiante_no_ayudante import EstudianteNoAyudante
from models.estudiante_ayudante import EstudianteAyudante
from models.estudiante_magister import EstudianteMagister
from models.estudiante_doctorado import EstudianteDoctorado
from models.alumni import Alumni
from db.db import DB

def main():
    # Crear asignaturas
    a1 = Asignatura("Cálculo", "CAL202", 7, "Pregrado")
    a2 = Asignatura("Simulación Avanzada", "SIMA301", 7, "Doctorado")
    a3 = Asignatura("Gestión de Proyectos", "GES201", 5, "Magister")
    a4 = Asignatura("Programación Funcional", "PROF401", 6, "Pregrado")
    a5 = Asignatura("Inteligencia Artificial", "IA501", 8, "Doctorado")
    
    DB.insertar_asignatura(a1)
    DB.insertar_asignatura(a2)
    DB.insertar_asignatura(a3)
    DB.insertar_asignatura(a4)
    DB.insertar_asignatura(a5)

    # Crear alumnos
    alumno1 = EstudianteNoAyudante("Nataniel Palacios", 25, "20175628-6", "2000-01-01")
    alumno2 = EstudianteAyudante("Simba Palacios", 2, "1111111-1", "2023-05-10")
    alumno3 = EstudianteMagister("Valentina Rojas", 27, "11223344-5", "1998-03-15")
    alumno4 = EstudianteDoctorado("Ignacio Fuentes", 30, "55667788-0", "1994-07-20")
    alumno5 = Alumni("Camila Soto", 28, "22334455-6", "1996-11-11")
    alumno6 = EstudianteNoAyudante("Sofía Martínez", 21, "33445566-7", "2004-09-22")

    DB.insertar_alumno(alumno1)
    DB.insertar_alumno(alumno2)
    DB.insertar_alumno(alumno3)
    DB.insertar_alumno(alumno4)
    DB.insertar_alumno(alumno5)
    DB.insertar_alumno(alumno6)

    # Asignar asignaturas
    alumno1.agregar_asignatura(a1)
    alumno2.agregar_asignatura(a1)
    alumno3.agregar_asignatura(a3)
    alumno4.agregar_asignatura(a2)
    alumno6.agregar_asignatura(a4)
    alumno6.agregar_asignatura(a5)

    # Descargar notas
    alumno1.descargar_notas()
    alumno4.descargar_notas()

    # Modificar alumno
    DB.modificar_alumno("11111111-1", nombre="Simba palacios")

    # Eliminar asignatura
    DB.eliminar_asignatura("SIMA301")

if __name__ == "__main__":
    main()