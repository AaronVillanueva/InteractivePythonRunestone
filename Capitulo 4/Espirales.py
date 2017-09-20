#coding: UTF-8
#Este programa dibuja una linea cuyo lado incrementa por 1 cada vez que termina su curso y gira.
#Posteriormente repite el proceso pero con un ángulo diferente
import turtle

def dibujarEspiral(t, ang):
    lado = 1
    for i in range(84):
        t.forward(lado)
        t.right(ang)
        lado = lado + 2


wn = turtle.Screen()
wn.bgcolor("lightgreen")

Maki = turtle.Turtle()
Maki.color('blue')

Maki.penup()
Maki.backward(110)
Maki.pendown()

dibujarEspiral(Maki, 90)

Maki.penup()
Maki.home()
Maki.penup()
Maki.forward(90)
Maki.pendown()

dibujarEspiral(Maki, 89)
wn.exitonclick()