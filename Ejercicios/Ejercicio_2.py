'''
Escribe una Clase que Convierta un Número Romano a Número Entero.
'''


class Roman_Numerals(object):
    # Atributo de Clase.
    dictNumber = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX", 10: "X"}

    # Constructor.
    def __init__(self, strNumber):
        self.strNumber = strNumber

    # Método de Instancia.
    def Convert(self):
        # Recorremos el Diccionario por los Valores.
        for i in range(1, len(self.dictNumber) + 1):
            if self.strNumber == self.dictNumber[i]:
                # Obtenemos las Llaves en un tipo 'dict_keys' que después convertiremos a Lista.
                self.listKeys = list(self.dictNumber.keys())
                # Le Restamos 1 dado que las Listas empiezan con el Índice 0.
                self.listKeys = self.listKeys[i - 1]

    def __str__(self):
        return "El Numero Romano {0} es el Numero Entero {1}".format(self.strNumber, self.listKeys)


if __name__ == '__main__':
    rn = Roman_Numerals("VII")
    rn.Convert()
    print(str(rn))