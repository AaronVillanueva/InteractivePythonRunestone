def parOnon(n):
    if n % 2 == 0:
        return (True)
    else:
        return (False)

x=int(input("Ingrese un número entero para determinar si es par: "))
print(parOnon(x))
