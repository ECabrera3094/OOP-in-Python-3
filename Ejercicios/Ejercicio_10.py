'''
Escribe una Clase Rectangulo que Obtenga una Base y Altura, y un Método que Devuelva el Área del Rectángulo.
'''


class Rectangle(object):

    def __init__(self, intBase, intHigh):
        self.intBase = intBase
        self.intHigh = intHigh
        self.area = 0

    def set_Area(self):
        self.area = (self.intBase * self.intHigh)

    def get_Area(self):
        return self.area

    # In Python property() is a Built-in Function that Creates and Returns a Property Object.
    # (get, set, del, doc)
    a = property( get_Area, set_Area )

    def __str__(self):
        return "El Area de un Rectangulo con Base {0} y Altura {1} es {2}.".format(self.intBase, self.intHigh, self.area)


if __name__ == '__main__':
    r = Rectangle(5, 9)
    r.set_Area()
    print("Get Area:", r.get_Area())
    print("Str:", str(r))
    print("property:", r.a)