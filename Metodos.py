class Employee:   

    # Atributo de Clase
    companyName = "Cognizant"

    salary = 500

    job = "AE"

    __tasa = 19
    
    # ATRIBUTOS == Variables de Instancia 
    def __init__(self):
        self.lastName = "Cabrera"
        self.__dia = 1

    # Metodo de Instancia.
    def instanceMethod(self):
        print("Metodo de Instancia - Compania: ", self.companyName)
        print("Metodo de Instancia - Apellido: ", self.lastName)
        self.instanceMethod_2()

    # Metodo de Instancia.
    def instanceMethod_2(self):
        self.lastName = "Lopez"
        print("Metodo de Instancia 2: " , self.lastName , "Sueldo: ", str(self.__tasa * self.salary))

    # Metodo de Clase
    @classmethod
    def classMethod(cls):
        cls.salary = 17000
        print("Metodo de Clase - Salario: ", cls.salary)
        print("Metodo de Clase - Compania: ", cls.companyName)
        print("Metodo de Clase - Tasa: ", cls.__tasa)
       
    # Metodo Estatico
    @staticmethod
    def staticMethod(num):
        # NO puede Tomar NINGUN Atributos.
        print("Solo es un Metodo Estatico " + num)

    # Metodo Publico
    def publicMethod(self):
        print("Publico")

    # Metodo Privado
    def __privateMethod(self):
        print("Privado")

   # Set Modifica las Varibles de Instancia
    def setDia(self, miDia):
        if (miDia > 0) and (miDia <= 31):
            self.__dia = miDia
            print("El dia es ", self.__dia)
        else:
            print("El dia NO Existe.")
    
    # Get Regresa las Variables de Instancia
    def getDia(self):
        return self.__dia
    


emy = Employee()
emy.instanceMethod()

print("******************")

Employee.classMethod()
emy.classMethod()

print("******************")

Employee.staticMethod("52")
emy.staticMethod("52")

print("******************")

emy.publicMethod()

print("******************")

emy.setDia(16)
print("Dia:", emy.getDia())