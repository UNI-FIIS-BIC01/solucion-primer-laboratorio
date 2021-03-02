import math

def primer_laboratorio():
    # Ingrese la solucion en las lineas subsiguientes.
    # INICIO
    primer_numero = int(input("Ingrese el valor de x: "))
    segundo_numero = int(input("Ingrese el valor de y: "))

    potencia = primer_numero ** segundo_numero
    print("x ** y = " + str(potencia))

    logaritmo = math.log(primer_numero, 2)
    print("log(x) = " + str(int(logaritmo)))
    # FIN
    return


# IMPORTANTE! No modificar de esta linea en adelante.
if __name__ == "__main__":
    primer_laboratorio()
