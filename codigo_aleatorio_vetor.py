import random

Estoque_Recondicionado_Dell = [f'notebook lote defeituoso: {i}'for i in range(1,21)]

alunos = []

for notebook in range(len(Estoque_Recondicionado_Dell)):
    sorteio = random.randint(1,19)
    notebook = sorteio
    alunos.append(Estoque_Recondicionado_Dell[notebook])

print(alunos)
