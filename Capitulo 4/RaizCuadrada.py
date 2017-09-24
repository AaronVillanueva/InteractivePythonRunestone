#Write a function called mySqrt that will approximate the square root of a number, call it n,
# by using Newton’s algorithm. Newton’s approach is an iterative guessing algorithm where the initial guess is n/2
# and each subsequent guess is computed using the formula: newguess = (1/2) * (oldguess + (n/oldguess)).

def raizCuadrada(n):
    primer = n/2
    segundo = (primer + n/primer)/2
    while segundo != primer:
        primer = segundo
        segundo = (primer + n/primer)/2
    return segundo

def Main():
    numero=float(input("Ingrese un número para obtener su raiz cuadrada: "))
    raizCalculada=raizCuadrada(numero)
    print(raizCalculada)

Main()