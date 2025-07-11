class Asignatura:
    def __init__(self, nombre: str, codigo: str, creditos: int, tipo: str = "General"):
        self.nombre = nombre
        self.codigo = codigo
        self.creditos = creditos
        self.tipo = tipo  # "Pregrado", "Magister", "Doctorado", "General"

    def __repr__(self):
        return f"{self.nombre} ({self.codigo}, {self.creditos} créditos, {self.tipo})"