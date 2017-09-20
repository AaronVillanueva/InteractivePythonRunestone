#coding: UTF-8
#Este programa crea un poligono de cuantos lados se le indique.
import turtle

wn = turtle.Screen()
wn.bgcolor("white")
Maki = turtle.Turtle()
Maki.color('red')
Maki.pensize(3)

def dibujarPoligono(t, numerolados, lado):
    for i in range(numerolados):
        t.forward(lado)
        t.left(360/numerolados)

def Main():
    lad=float(input("Ingrese el valor del lado del poligono"))
    num=int(input("Ingrese el número de lados"))
    dibujarPoligono(Maki, num, lad)

Main()