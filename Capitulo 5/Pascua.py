#encoding: UTF-8

def analisisPascua(year):
    a = year % 19
    b = year % 4
    c = year % 7
    d = (19*a + 24) % 30
    e = (2*b + 4*c + 6*d + 5) % 7
    fecha = 22 + d + e
    if year == 1954 or year == 2981 or year == 2049 or year == 2076:
        fecha = fecha - 7
    return(fecha)

def Main():
    year = int(input("Introduce un año desde 1900 hasta 2099: "))
    if year >= 1900 and year <= 2099:
        pascua=analisisPascua(year)
        if pascua > 31:
            print("Abril", pascua - 31)
        else:
            print("Marzo", pascua)
    else:
        print("Eror. Año fuera del rango")

Main()