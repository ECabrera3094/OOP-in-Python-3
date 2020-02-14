'''
Escribe una Clase que Calcule pow(x, n)
x = es la base
n = es el exponente

Entrada: pow(2, -3)
Salida: 0.125
'''


class Pow(object):

    # Constructor.
    def __init__(self, x, n):
        self.x = x
        self.n = n

    # Método de Instancia.
    def findPow(self):
        self.ans = (self.x ** self.n)

    def __str__(self):
        return "Entrada: ({0}, {1}). Salida: {2}.".format( self.x, self.n, self.ans )


if __name__ == '__main__':
    p = Pow(2, -3)
    p.findPow()
    print(str(p))