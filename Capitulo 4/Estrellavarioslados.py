#Encoding; UTF-8
import turtle
Maki = turtle.Turtle()

def dibujarEstrella(t, n):
    for i in range(n):
        t.forward(100)
        t.left(180 - 180/n)
def Main():
    numeroDeLados=int(input("Ingrese el número de lados de la estrella: "))
    dibujarEstrella(Maki, numeroDeLados)

Main()