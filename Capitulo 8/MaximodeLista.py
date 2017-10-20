import random

lista = []
for i in range(100):
    lista.append(random.randint(0, 1000))
    
def max(l):
    max = 0
    for i in l:
        if i > max:
            max = i
    return (max)

print(max(lista))
