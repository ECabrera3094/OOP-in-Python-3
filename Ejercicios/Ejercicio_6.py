'''
Escribir una Clase que Encuentre los 3 Elementos que Sumen 0 a partir de Números Reales.
Entrada: [-25, -10, -7, -3, 2, 4, 8, 10]
Salida: [[-10, 2, 8], [-7, -3, 10]]
'''


class Find(object):

    def __init__(self, list_Enter):
        self.listEnter = list_Enter
        self.listOut = []

    def set_Zero(self):
        for i in range(len(self.listEnter)):
            j = i + 1
            for j in range(j, len(self.listEnter)):
                k = j + 1
                for k in range(k, len(self.listEnter)):
                    if (self.listEnter[i] + self.listEnter[j] + self.listEnter[k] == 0):
                        self.listOut.append( [self.listEnter[i], self.listEnter[j], self.listEnter[k]] )

    def get_Zero(self):
        return self.listOut

    def __str__(self):
        return "{0}".format(self.listOut)

    sum_Zero = property(get_Zero, set_Zero)


if __name__ == '__main__':
    f = Find( [-25,-10,-7,-3,2,4,8,10] )
    f.set_Zero()
    print("Get:      ", f.get_Zero())
    print("Property: ", f.sum_Zero)
    print("STR:      ", str(f))