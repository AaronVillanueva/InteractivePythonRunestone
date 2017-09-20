#coding: UTF-8
#Este programa dibuja una linea cuyo lado incrementa por 1 cada vez que termina su curso y gira.
#Posteriormente repite el proceso pero con un ángulo diferente
import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")

Maki = turtle.Turtle()
Maki.color('blue')
Maki.speed(20)
Maki.hideturtle()

def dibujarEspiral(t, ang):
    lado = 1
    for i in range(84):
        t.forward(lado)
        t.right(ang)
        lado = lado + 2

def retroceso(Maki):
    Maki.penup()
    Maki.backward(110)
    Maki.pendown()

def reposicionamiento():
    Maki.penup()
    Maki.home()
    Maki.penup()
    Maki.forward(90)
    Maki.pendown()

def Main():
    retroceso(Maki)
    dibujarEspiral(Maki, 90)
    reposicionamiento()
    dibujarEspiral(Maki, 89)

Main()
wn.exitonclick()

