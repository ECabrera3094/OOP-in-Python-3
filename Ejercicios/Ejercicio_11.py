'''
Escribe una Clase Circulo que contenga un Radio, con un Método que Devuelva el Área y otro que Devuelva el Perímetro.
'''
from math import pi

class Circle(object):

    def __init__(self, intRadius):
        self.intRadius = intRadius
        self.intArea = 0
        self.intPerimeter = 0

    def set_Area(self):
        self.intArea = pi * (self.intRadius ** 2)

    def get_Area(self):
        return self.intArea

    def set_Perimeter(self):
        self.intPerimeter = (2 * pi) * self.intRadius

    def get_Perimeter(self):
        return self.intPerimeter

    area = property(get_Area, set_Area)
    perimeter = property(get_Perimeter, set_Perimeter)

    def __str__(self):
        return "El Area del Circulo es {0} y su Pewrimetro es {1}.".format(self.area, self.perimeter)
# http://www.pythondiario.com/2015/11/ejercicios-de-clases-y-objetos-en.html

if __name__ == '__main__':
    c = Circle(3)
    c.set_Area()
    print("Get: ", c.get_Area())
    c.set_Perimeter()
    print("Get: ", c.get_Perimeter())
    print("property", c.area)
    print("property", c.perimeter)
    print("STR: ", str(c))