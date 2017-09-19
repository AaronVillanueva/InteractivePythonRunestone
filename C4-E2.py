#Este programa dibuja un patron cuadrado donde cada cuadrado es 20 unidades mas grande que el anterior.

import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")

turtle.color("purple")

def dibujarCuadrado (lado):
    for i in range(4):
        turtle.forward(lado)
        turtle.left(90)

def figura(lad,sep):
    for i in range(9):
        dibujarCuadrado(lad)
        turtle.forward(lad)
        turtle.penup()
        turtle.forward(sep)
        turtle.left(90)
        turtle.backward(sep)
        turtle.pendown()
        lad+=20

def Main():
    lado = 20
    separacion = 10
    figura(lado,separacion)

Main()
wn.exitonclick()