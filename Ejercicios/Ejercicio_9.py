'''
Escribe una Clase con 2 Métodos: get_string y print_string.
get_string acepta una Cadena Ingresada por el usuario y print_string Imprime la Cadena en Mayúsculas.
'''


class Cadena(object):

    def __init__(self):
        pass

    def get_String(self, strCadena):
        self.strCadena = strCadena
        self.strCadena = self.strCadena.upper()

    def print_String(self):
        return self.strCadena


if __name__ == '__main__':
    c = Cadena()
    c.get_String("Hola Mundo")
    print(c.print_String())