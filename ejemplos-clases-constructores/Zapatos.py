class zapatos:    
    def __init__(self, marca, precio):
        self.marca = marca
        self.precio = precio

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Especie: {self.especie}")
        print(f"Edad: {self.edad} años")

mar = "Adidas"
pre = 125
zap = zapatos(mar, pre)
zap.mostrar_informacion()