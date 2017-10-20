#encoding: UTF-8
def numeroPrimo(n):
    if n%2==0 or n%3==0 or n%5==0:
        conclusion=False
    else:
        conclusion=True
    return(conclusion)

def Main():
    x=int(input("Ingrese un número entero: "))
    final=numeroPrimo(x)
    print(final)

Main()
