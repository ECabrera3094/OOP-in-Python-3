'''
Escribe una Clase que obtenga TODOS los Posibles Subconjuntos Únicos de un Conjunto de Números Enteros Distintos.
Entrada: [4, 5, 6]
Salida: [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]
'''

class Subconjuntos:

    def __init__(self, conjunto):
        self.conjunto = conjunto

    def subconj(self):
        sub = [[], self.conjunto]
        corta = 0
        for prim in self.conjunto:
            print("prim ",prim)
            corta += 1
            sub += [[prim]]
            for sec in self.conjunto[corta:]:
                print("Conjunto: ", self.conjunto[corta:], "corta: ", corta)
                sub += [[prim, sec]]
                print("Sub: ", sub)

        return sub

s = Subconjuntos([4,5,6])

print(s.subconj())