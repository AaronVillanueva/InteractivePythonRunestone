import random

def sumarNegativos(l):
    contador = 0
    for i in l:
        if i < 0:
            contador = contador + i
    return contador

lista = []
for i in range(100):
    lista.append(random.randrange(-1000, 1000))

print(sumarNegativos(lista))
