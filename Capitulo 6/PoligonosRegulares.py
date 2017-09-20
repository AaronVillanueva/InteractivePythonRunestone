#coding: UTF-8

#Triangulo

import turtle
wn = turtle.Screen()
Andii = turtle.Turtle()

for i in range(3):
    Andii.forward(100)
    Andii.left(360/3)

wn.exitonclick()

#Cuadrado
import turtle

wn = turtle.Screen()
Mel = turtle.Turtle()

for i in range(4):
    Mel.forward(100)
    Mel.left(360/4)

wn.exitonclick()

# Hexagono
import turtle

wn = turtle.Screen()
Maki = turtle.Turtle()

for i in range(6):
    Maki.forward(100)
    Maki.left(360/6)

wn.exitonclick()

#Octagono
import turtle
wn = turtle.Screen()
Isa = turtle.Turtle()
#Este forward(20) permite que la mitad del octagono se encuentre en la mitad del cuadrado
Isa.forward(20)
for i in range(8):
    Isa.forward(60)
    Isa.left(360/8)

wn.exitonclick()
