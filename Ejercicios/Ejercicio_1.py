'''
Escribe una Clase que Convierta un Número Entero a Número Romano.
'''


class Roman_Numerals(object):

    # Atributo de Clase.
    dictNumber = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX", 10: "X"}

    # Constructor.
    def __init__(self, intNumber):
        # Variable de Instancia.
        self.intNumber = intNumber

    # Método de Instancia.
    def Convert(self):
        # Recorremos el Diccionario por las Llaves.
        for number in self.dictNumber:
            if self.intNumber == number:
                # get() regresa el Valor según la Llave asignada.
                print("El Numero {0} en Romano es {1}".format(self.intNumber, self.dictNumber.get(number)))


if __name__ == '__main__':
    rn = Roman_Numerals(6)
    rn.Convert()