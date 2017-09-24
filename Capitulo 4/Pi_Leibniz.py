#Consultar https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80

def calcularPi(rango):
    pi = 0
    signo = 1
    denominador = 1
    for i in range(rango):
        pi = pi + (signo/denominador)
        signo = signo * -1
        denominador = denominador + 2
    pi = pi * 4.0
    return (pi)
def Main():
    aproximacionPi = calcularPi(10000)
    print(aproximacionPi)

Main()