def count(obj, l):
    count = 0
    for e in l:
        if e == obj:
            count = count + 1
    return count

def is_in(obj, l):
    for e in l:
        if e == obj:
            return True
    return False

def reverse(lst):
    reversa = []
    for i in range(len(lst)-1, -1, -1):
        reversa.append(lst[i])
    return reversa

def index(obj, l):
    for i in range(len(l)):
        if l[i] == obj:
            return i
    return (-1)

def insert(obj, index, l):
    nuevaLista = []
    for i in range(len(l)):
        if i == index:
            nuevaLista.append(obj)
        nuevaLista.append(l[i])
    return nuevaLista

lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(count(1, lst))
print(is_in(4, lst))
print(reverse(lst))
print(index(2, lst))
print(insert('meme', 4, lst))
