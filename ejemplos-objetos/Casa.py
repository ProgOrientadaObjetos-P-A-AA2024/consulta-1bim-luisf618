class casa:
    def __init__(self, color, year):
        self.color = color
        self.year = year

    def describir(self):
        print(f"Casa de color {self.color} y creada en {self.year}")

casa1 = casa("blanca","2015")
casa1.decribir()   