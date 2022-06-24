lista = [5,10]

def Potencia(lista):
    n = 0
    while n < len(lista):
        yield lista[0]**2 
        yield lista[1]**2
        n += 2
        
objeto = Potencia(lista)

print(list(objeto))
