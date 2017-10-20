import random
lista=[]
for i in range(100):
    lista.append(random.randint(0,1000))
promedio=sum(lista) /100
print(promedio)
