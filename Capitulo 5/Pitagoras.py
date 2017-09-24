#encoding: UTF-8

def hipotenusa(x,y):
    hip=((x**2)+(y**2))**.5
    return(hip)

def Main():
    primernumero=float(input("Ingrese un lado del triángulo: "))
    segundonumero=float(input("Ingrese el otro lado del triángulo: "))
    final=hipotenusa(primernumero,segundonumero)
    print("La hipotenusa del triángulo es:",final)

Main()