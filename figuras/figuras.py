from punto import Punto
from math import pi

class Figura:

    def __init__(self, punto1, punto2):
        self.origen = punto1
        self.fin = punto2
        self.area = 0
        self.perimetro = 0

    def calcular_area(self):
        pass

    def calcular_perimetro(self):
        pass

    def informar_propiedades(self):
        print("tipo figura ", str(type(self)).split(".")[1][:-2])
        print("el area es ", self.area)
        print("el perimetro es ", self.perimetro)


class Cuadrado(Figura):

    def calcular_area(self):
        lado = self.origen.calcular_distancia(Punto(self.fin.x,self.origen.y))
        self.area = lado * lado

    def calcular_perimetro(self):
        lado = self.origen.calcular_distancia(Punto(self.fin.x,self.origen.y))
        self.perimetro = 4 * lado

class Rectangulo(Figura):

    def calcular_area(self):
        base = self.origen.calcular_distancia(Punto(self.fin.x,self.origen.y))
        altura = self.origen.calcular_distancia(Punto(self.origen.x,self.fin.y))
        self.area = base * altura

    def calcular_perimetro(self):
        base = self.origen.calcular_distancia(Punto(self.fin.x,self.origen.y))
        altura = self.origen.calcular_distancia(Punto(self.origen.x,self.fin.y))
        self.perimetro = 2 * (base + altura)

class Triangulo(Figura):

    def calcular_area(self):
        base = self.origen.calcular_distancia(Punto(self.fin.x,self.origen.y))
        altura = self.origen.calcular_distancia(Punto(self.origen.x,self.fin.y))
        self.area = base * altura / 2

    def calcular_perimetro(self):
        base = self.origen.calcular_distancia(Punto(self.fin.x,self.origen.y))
        altura = self.origen.calcular_distancia(Punto(self.origen.x,self.fin.y))
        hipo = self.origen.calcular_distancia(self.fin)
        self.perimetro = base + altura + hipo

class Circulo(Figura):

    def calcular_area(self):
        radio = self.origen.calcular_distancia(self.fin)
        self.area = pi * radio ** 2

    def calcular_perimetro(self):
        radio = self.origen.calcular_distancia(self.fin)
        self.perimetro = 2 * pi * radio


if __name__ == "__main__": 
    f =  Cuadrado(Punto(5,10), Punto(10,15))
    f.calcular_area()
    f.calcular_perimetro()
    f.informar_propiedades()
    