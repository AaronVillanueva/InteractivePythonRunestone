import random

def contarNones(l):
    contador = 0
    for i in l:
        if i % 2 != 0:
            contador = contador + 1
    return (contador)

lista = []
for j in range(100):
    lista.append(random.randint(0, 1000))

print(contarNones(lista))
