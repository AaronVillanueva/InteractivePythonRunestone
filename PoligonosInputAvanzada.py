#coding: UTF-8
#Que hace
import turtle

def dibujarPoligono(lados,longitud,color,relleno):
  turtle.color(color)
  turtle.fillcolor(relleno)
  turtle.begin_fill()
  for i in range(lados):
    turtle.forward(longitud)
    turtle.left(360/lados)
  turtle.end_fill()
  
def Main():
  numeroLados=int(input("Ingrese el numero de lados"))
  longitudLado=float(input("Ingrese la longitud del lado"))
  colorpluma=str.lower(input("Ingrese el color del lado"))
  colorrelleno=str.lower(input("Ingrese el color de relleno"))
  dibujarPoligono(numeroLados,longitudLado,colorpluma,colorrelleno)

Main()
