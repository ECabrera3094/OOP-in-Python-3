class Persona(object): # 'Object' porque esta NO Hereda de Nadie.

    def __init__(self, cedula, nombre, apellido, sexo):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo

    def hablar(self, mensaje):
        return mensaje

    def getGenero(self, sexo):
        genero = ['Masculino', 'Femenino']

        if sexo == 'M':
            return genero[0]
        elif sexo == 'F':
            return genero[1]

    # El método __str__ es un método usando para imprimir la descripción de la instancia de objeto
    def __str__(self):
        return "%s, %s, %s, %s" % (
            str(self.cedula), self.nombre, self.apellido, self.sexo
        )

class Nomina(object):

    def __init__(self, nomina):
        self.nomina = nomina 

    def consulta_Nomina(self):
        return self.nomina


class Supervisor(Persona, Nomina): # Hereda de la Clase Persona y Nomina

    def __init__(self, cedula, nombre, apellido, sexo, rol, nomina):
        # Invoca al constructor de Clase Persona.
        Persona.__init__(self, cedula, nombre, apellido, sexo)
        # Invoca al constructor de Clase Nomina.
        Nomina.__init__(self, nomina)
        
        self.rol = rol
        self.tarea = ['10', '11', '12']

    def consulta_Tarea(self):
        return ', '.join(self.tarea)

    # El método __str__ es un método usando para imprimir la descripción de la instancia de objeto
    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s" % (
            str(self.cedula), self.nombre, self.apellido, self.sexo, self.rol, self.consulta_Tarea(), self.consulta_Nomina()
        )

if __name__ == '__main__':

    p1 = Persona('12345', 'Emiliano', 'Cabrera', 'M')
    print( p1.getGenero(p1.sexo) )
    print( p1.hablar("Hola Amigos.") )
    print( str(p1) )

    p2 = Supervisor('67890', 'Gabriela', 'Canales', 'F','PM', '17,000')
    print( p2.getGenero(p2.sexo) )
    print( p2.hablar("Hola Amigas.") )
    print( str(p2) )