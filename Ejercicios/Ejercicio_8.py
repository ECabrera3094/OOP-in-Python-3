'''
Escribe una Clase que Revierta una Cadena de Palabras.
Entrada: "Mi Diario Python"
Salida: "Python Diario Mi"
'''


class Reverse(object):

    # Constructor.
    def __init__(self, strCadena):
        self.strCadena = strCadena
        self.list_Cadena = self.strCadena.split(" ")
        self.newCadena = []

    # Método de Instancia.
    def reverse(self):
        for i in range( 0, len(self.list_Cadena) ):
            self.newCadena.append( self.list_Cadena[(i+1) * -1] )
        self.newCadena = ' '.join(self.newCadena)

    def __str__(self):
        return "Entrada: {0}. Salida: {1}.".format(self.strCadena, self.newCadena)


if __name__ == '__main__':
    r = Reverse("Mi Diario Python")
    r.reverse()
    print(str(r))