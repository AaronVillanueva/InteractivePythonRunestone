#Encoding: UTF-8
import turtle
Maki = turtle.Turtle()

def dibujarEstrella(t, n):
    for i in range(n):
        t.forward(100)
        t.left(180 - 180/n)
def paresYnones(numeroPrueba):
    numeroProbacion=numeroPrueba%2
    if numeroProbacion==0:
        conclusion=False
    else:
        conclusion=True
    return(conclusion)

def Main():
    numeroDeLados=int(input("Ingrese un número impar mayor a 3 para dibujar una estrella"))
    if numeroDeLados<=2:
        print("No hay suficientes lados")
    else:
        lados=paresYnones(numeroDeLados)
        if lados==True:
            dibujarEstrella(Maki, numeroDeLados)
        else:
            print("Favor de ingresar un número impar")

Main()