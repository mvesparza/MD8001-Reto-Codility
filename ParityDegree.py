"""
Programa que encuentra la potencia más alta de 2 que divide N.

Autor: Marco Vinicio Esparza

Versión: v1.3
"""

import big_o

def solucion(N):
    """
    Proceso que cuenta el número de veces que se puede dividir un número entero N por
    2 antes de obtener un número impar.
    Parámetros:
    --------------
    Si, recibe un parámetro N como entero ingresado por el usuario.

    Retorna:
    --------------
    Si, retorna el resultado generado.
    """
    resultado = 0  # Inicializa la variable "resultado" en 0
    while not N & 1:   # Mientras el bit menos significativo de N sea 0 
        resultado += 1  # Incrementa en 1 el valor de resultado
        N =  N >> 1    # Desplaza N un bit a la derecha
    return resultado  # Devuelve el valor de resultado


if __name__ == '__main__':
    # inicializo el programa
    print("********* Encuentra la potencia más alta de 2 que divide N *********")
    # inicio bucle para repetir el proceso las veces que el usuario quiera
    while(True):
        # declaro una variable global
        N = int(input("Ingrese un entero: "))
        r = solucion(N)
        potencia = 2**r
        print("El resultado es:", r)
        print("Porque la potencia más alta de 2 que divide", N, "es 2 ^","(",r,")", "=", potencia)

        # Variable para calcular la complejidad
        num = lambda n: potencia
        # calculo la Complejidad en el tiempo de la funcion
        best, others = big_o.big_o(solucion, num)
        verificarComplejidad = input("Desea verificar la complejidad en el tiempo de la funcion? (si/no): ")
        if verificarComplejidad.lower() == "si":
            print(best)
        
        # pregunto si quiere volver a usar el programa  
        repetirProceso = input("Repetir proceso? (si/no): ")
        if repetirProceso.lower() != "si":
            print("********** FIN DEL PROGRAMA **********")
            # detengo el bucle por completo
            break