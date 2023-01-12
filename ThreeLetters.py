"""
Programa que dados dos enteros A y B, devuelve una cadena que contenga letras A "a" y letras
B "b" sin que tres letras consecutivas sean iguales.

Autor: Marco Vinicio Esparza

Versión: v2.2
"""

import big_o

def solucion(A, B):
    """
    Proceso que condiciona las entrada A y B, para generar cadenas con "a" ó "b"
    Parámetros:
    --------------
    Si, recibe un parámetro A y B como enteros.
    A: es el número de "a"
    B: es el número de "b"
    Retorna:
    --------------
    Si, retorna el costo del ticket.
    """
    # Si A es igual a 0 se retorna B veces la letra 'b'
    if A == 0:
        return 'b' * B
    # Si B es igual a 0 se retorna A veces la letra 'a'
    if B == 0:
        return 'a' * A
    # si A es 1 y B es 1 se retorna 'ab'
    if A == 1 and B == 1:
        return 'ab'
    # si A es mayor que B se retorna 'aab' concatenado con la llamada recursiva de la función con A-2 y B-1
    if A > B:
        return 'aab' + solucion(A-2, B-1)
    # si no se retorna 'bba' concatenado con la llamada recursiva de la función con A-1 y B-2
    return 'bba' + solucion(A-1, B-2)

if __name__ == '__main__':
    # inicializo el programa
    print("********* Tres Letras *********")
    # inicio bucle para repetir el proceso las veces que el usuario quiera
    while(True):
        # declaro una variable global
        # Pedir al usuario que ingrese A y B
        A = int(input("Ingrese el valor de A: "))
        B = int(input("Ingrese el valor de B: "))
        # Mostrar resultado en pantalla
        resultado = solucion(A, B)
        print("Se genera: ", resultado)
    
        num = lambda n: A
        num1 = lambda j: B
        # calculo la Complejidad en el tiempo de la funcion
        best, others = big_o.big_o(num, num1)
        verificarComplejidad = input("Desea verificar la complejidad en el tiempo de la funcion? (si/no): ")
        if verificarComplejidad.lower() == "si":
            print(best)

        # pregunto si quiere volver a usar el programa
        repetirProceso = input("Repetir proceso? (si/no): ")
        if repetirProceso.lower() != "si":
            print("********** FIN DEL PROGRAMA **********")
            # detengo el bucle por completo
            break