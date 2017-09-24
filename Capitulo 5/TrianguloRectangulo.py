#encoding: UTF-8

def encontrarHipotenusa(x,y,z):
    if x>y and x>z:
        hipotenusa=x
        cateto=y
        cateto2=z
    elif y>x and y>z:
        hipotenusa=y
        cateto=x
        cateto2=z
    elif z>x and z>y:
        hipotenusa=z
        cateto=x
        cateto2=y
    return(cateto,cateto2,hipotenusa)

def analisisDeLados(x,y,hip):
    x=x**2
    y=y**2
    z=x+y
    z=z**.5
    if abs(hip-z)<.01:
        return(True)
    else:
        return(False)

def Main():
    primerlado=float(input("Ingrese el primer lado del triángulo: "))
    segundolado=float(input("Ingrese el segundo lado del triángulo: "))
    tercerlado=float(input("Ingrese el tercer lado del triángulo: "))
    ladoA,ladoB,ladoC=encontrarHipotenusa(primerlado,segundolado,tercerlado)
    conclusion=analisisDeLados(ladoA,ladoB,ladoC)
    print(conclusion)
    if conclusion==True:
        print("Los lados provistos indican que el triángulo es rectángulo")
    else:
        print("Los lados provistos indican que el triángulo no es rectángulo")

Main()