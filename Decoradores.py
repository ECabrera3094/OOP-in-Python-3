# Decorador
def decorador(funcion_a_decorar):
    def complemento():
        print("Accion 1.")
        funcion_a_decorar()
        print("Accion 2.")
    return complemento

@decorador
def mensaje():
    print("Hola Mundo.")

if __name__ == '__main__':
    m = mensaje()

#--------------------------------