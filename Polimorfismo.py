class Gato():

    def __init__(self):
        self.nombre = 'Misha'
        self.edad = 10

    def hablar(self):
        print("MIAU")

    def comer(self):
        print("NOM NOM")

class Perro():

    def __init__(self):
        self.nombre = 'Titan'
        self.edad = 12

    def hablar(self):
        print("GUAU")

    def comer(self):
        print("NAM NAM")

class Mascota(Gato, Perro):

    def __init__(self):
        Perro.__init__(self)
        Gato.__init__(self)

    def escuchar(self, animal):
        animal.hablar()

    def comer(self, animal):
        animal.comer()

if __name__ == '__main__':

    p = Perro()
    g = Gato()

    animal = Mascota()
    animal.escuchar(p)
    animal.escuchar(g)
    animal.comer(p)
    animal.comer(g)