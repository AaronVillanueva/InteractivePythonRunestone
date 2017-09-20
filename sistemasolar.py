import turtle
import threading
from threading import Thread
turtle.bgcolor("black")

diasMercurio=87.969
diasVenus=224.7
diasTierra=365.2564
diasMarte=687
diasJupiter=4332.59
diasSaturno=10759
diasUrano=30688.5
diasNeptuno=60182

def posicionInicial(t,orden):
    t.penup()
    t.right(90)
    t.forward(50*orden)
    t.left(90)
    t.pendown()
    t.showturtle()

Sol=turtle.Turtle()
Mercurio=turtle.Turtle()
Venus=turtle.Turtle()
Tierra=turtle.Turtle()
Marte=turtle.Turtle()
Jupiter=turtle.Turtle()
Saturno=turtle.Turtle()
Urano=turtle.Turtle()
Neptuno=turtle.Turtle()

def movimientoCircular(t,dias,orden):
    t.speed(365/dias)
    for i in range (1):
        t.circle(50*orden)

def planeta(t,dias,orden,color):
    t.shape("circle")
    t.color(color)
    t.hideturtle()
    posicionInicial(t,orden)
    t.showturtle()
    movimientoCircular(t,dias,orden)

def planeta2(t,dias,orden,color):
    t.shape("circle")
    t.color(color)
    t.hideturtle()
    posicionInicial(t,orden)
    t.showturtle()
    movimientoCircular(t,dias,orden)

def Main():
    Sol.shape("circle")
    Sol.color("yellow")
    planeta(Mercurio,diasMercurio,1,"brown")
    planeta2(Venus,diasVenus,2,"white")
    planeta(Tierra,diasTierra,3,"green")
    planeta(Marte,diasMarte,4,"red")
    planeta(Jupiter,diasJupiter,5,"brown")
    planeta(Saturno,diasSaturno,6,"yellow")
    planeta(Urano,diasUrano,7,"#00008B")
    planeta(Neptuno,diasNeptuno,8,"#00008B")

Main()