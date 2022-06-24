def fibo(n):
    penultimo=1
    ultimo=1
    
    if (n==1) or (n==2):
        print("1")
    else:
        count=3
        while count <= n:
            # olhando para a estrutura de cima voce percebe como os valores devem se comportar...
            # se o proximo se tornou o último, então o penultimo tem que ser o novo ultimo 
            proximo = ultimo + penultimo #2
            penultimo = ultimo #1
            ultimo = proximo #2
            
            count += 1
            yield (proximo)

n = 10
interavel = fibo(n)
lista = []

for i in interavel:
    lista.append(i)
print(lista)
