def raizCuadrada(n):
    aprox = 0.5 * n
    mejor = 0.5 * (aprox + n/aprox)
    while mejor != aprox:
        aprox = mejor
        mejor = 0.5 * (aprox + n/aprox)
        print("Approx:", mejor)
    return (aprox)

def Main():
    print("Raiz aproximada:", raizCuadrada(25))

Main()
