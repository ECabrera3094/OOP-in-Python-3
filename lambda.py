# Conocida tambien como FUNCION ANONIMA

# def to_do(a): return a * 2

# Funcion =  Lambda [entrada] : [proceso]
b = lambda a : a * 2
print("B: ", b(5))

dolar = lambda num : num * 20.00
print("Dolar: ", dolar(2))

# ------------------------------------------------

lista_1 = lambda letras, i : letras[i] + " AQUI"
    
letras = ["E", "M", "Y"]
for i in range(len(letras)): 
    print( "> Forma 1: ", lista_1( letras, i ) )

# ------------------------------------------------

lista_1 = lambda letras, i : letras[i] + " AQUI"
    
letras = ["E", "M", "Y"]
new_letras = []
for i in range(len(letras)):
    new_letras.append( lista_1(letras, i )) 

print("> Forma 2: ", new_letras)

# ------------------------------------------------

a = ["A", "C", "B", "A"]
b = list (map (lambda x : x == "A", a) )
c = list (filter (lambda x : x == "A", a) )
print("MAP: ", b)
print("FILTER: ", c)