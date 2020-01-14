class Persona(object):

    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

class Estudiante(Persona):

    def __init__(self,  nombre, edad, genero, matricula):
        Persona.__init__(self, nombre, edad, genero)
        self.matricula = matricula

class Facultad(Persona):

    def __init__(self,  nombre, edad, genero, lunch, bono):
        Persona.__init__(self, nombre, edad, genero)
        self.lunch = lunch
        self._bono = bono

    def getBono(self):
        return self._bono


class TA(Estudiante, Facultad):

    def __init__(self,  nombre, edad, genero, matricula, lunch, bono):
        Estudiante.__init__(self,  nombre, edad, genero, matricula)
        Facultad.__init__(self,  nombre, edad, genero, lunch, bono)

    def __str__(self):
        
        return '%s, %s, %s, %s, %s, %s' % (
            self.nombre, self.edad, self. genero, self.matricula, self.lunch, self._bono
        )

if __name__ == '__main__':

    ta = TA('Emiliano', '25', 'M', '2013350682', 'Pollo', '1000')
    print( str(ta) )