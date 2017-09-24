#Consultar https://en.wikipedia.org/wiki/Madhava_of_Sangamagrama

def calcularPi(rango):
    pi = 1
    signo = 1
    denominador = 3
    aumento=1
    for i in range(rango):
        pi = pi - (signo/(denominador*(3**aumento)))
        signo = signo * -1
        denominador = denominador + 2
        aumento=aumento+1
    pi = pi * (12**.5)
    return (pi)
def Main():
    aproximacionPi = calcularPi(21)
    print(aproximacionPi)

Main()