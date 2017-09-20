#encodings: UTF-8

def calificacion(valor):
    if valor >= 90:
        return "A"
    else:
        if valor >= 80:
            return "B"
        else:
            if valor >= 70:
                return "C"
            else:
                if valor >= 60:
                    return "D"
                else:
                    return "F"

puntaje=float(input("Ingrese su calificación del 1 al 100: "))
print( "Su calificación es", calificacion(puntaje))