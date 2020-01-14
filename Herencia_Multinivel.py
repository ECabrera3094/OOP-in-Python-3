class Persona(object):

    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

class Estudiante(Persona):

    def __init__(self, nombre, edad, genero, matricula):
        Persona.__init__(self, nombre, edad, genero)
        self.matricula = matricula

    def __str__(self):
        return '%s, %s, %s, %s' % (
            self.nombre, self.edad, self.genero, self.matricula
        )

class TA(Estudiante):

    def __init__(self, nombre, edad, genero, matricula, salario):
        Estudiante.__init__(self, nombre, edad, genero, matricula)
        self.salario = salario

    def __str__(self):
        return '%s, %s, %s, %s, %s' % (
            self.nombre, self.edad, self.genero, self.matricula, self.salario
        )

if __name__ == '__main__':

    ta = TA('Emiliano', '25', 'M', '2013350682', '17000')
    print( str(ta) )

    es = Estudiante('Emiliano', '25', 'M', '2013350682')
    print( str(es) )