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

    # El Método __str__ es usando para Imprimir la Descripción de la Instancia de Objeto.
    def __str__(self):
        return "%s, %s, %s, %s" % (
            str(self.cedula), self.nombre, self.apellido, self.sexo
        )

class Supervisor(Persona): # Hereda de la Clase Persona

    def __init__(self, cedula, nombre, apellido, sexo, rol):
        # Invoca al constructor de Clase Persona.
        Persona.__init__(self, cedula, nombre, apellido, sexo)
        
        self.rol = rol
        self.tarea = ['10', '11', '12']

    def consulta_Tarea(self):
        return ', '.join(self.tarea)

    # El método __str__ es usando para Imprimir la Descripción de la Instancia de Objeto.
    def __str__(self):
        return "%s, %s, %s, %s, %s, %s" % (
            str(self.cedula), self.nombre, self.apellido, self.sexo, self.rol, self.consulta_Tarea()
        )

if __name__ == '__main__':

    p1 = Persona('12345', 'Emiliano', 'Cabrera', 'M')
    print( p1.getGenero(p1.sexo) )
    print( p1.hablar("Hola Amigos.") )
    print( str(p1) )

    p2 = Supervisor('67890', 'Gabriela', 'Canales', 'F', 'PM')
    print( p2.getGenero(p2.sexo) )
    print( p2.hablar("Hola Amigas.") )
    print( str(p2) )