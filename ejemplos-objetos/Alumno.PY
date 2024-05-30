class alumno:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def registro(self):
        print(f"HEstudiante {self.nombre} con edad de {self.edad} años")

alumno1 = alumno("Josue", 18)
alumno1.registro()