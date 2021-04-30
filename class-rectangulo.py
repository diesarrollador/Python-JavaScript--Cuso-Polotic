# Escribe una clase de Python llamada Rectangulo que se define por una
# longitud y un ancho y un método que calculará el área de un rectángulo.
class Rectangulo():
    def __init__(self, longitud, ancho):
        self.longitud = longitud
        self.ancho = ancho
        
    def calcular(self):
       return self.longitud * self.ancho