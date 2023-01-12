"""
Programa que encuentra el primer número único en una secuencia dada.

Autor: Marco Vinicio Esparza

Versión: v3.2
"""

import big_o

def solucion(A):
    """
    Proceso que identifica el número que no se repite de una lista ingresada
    Parámetros:
    --------------
    Si, recibe un parámetro A como entero y que es el tamaño de la matriz.

    Retorna:
    --------------
    Si, retorna el primer número que no se repite y -1 si es que todos los
    números se repiten.
    """
    frecuencia = {}
    #recorrer matriz A y guardar la frecuencia de cada número en el diccionario
    for num in A:
        if num in frecuencia:
            frecuencia[num] += 1
        else:
            frecuencia[num] = 1
    #recorrer matriz A nuevamente y devolver el primer número único
    for i in range(len(A)):
        if frecuencia[A[i]] == 1:
            return A[i]
    #si no se encuentra un número único, devolver -1
    return ("Todos los números se repiten", -1)

if __name__ == '__main__':
    # inicializo el programa
    print("********* Encuentra el primer número único en una secuencia dada *********")
    # inicio bucle para repetir el proceso las veces que el usuario quiera
    while(True):
        # declaro una variable global
        N = int(input("Ingrese el tamaño de la matriz A: "))
        A = [int(input("Ingrese el elemento {} de la matriz A: ".format(i+1))) for i in range(N)]
        print("Primer único número: ", solucion(A))
    
        # Variable para calcular la complejidad
        num = lambda n: A
        # calculo la Complejidad en el tiempo de la funcion
        best, others = big_o.big_o(solucion, num)
        verificarComplejidad = input("Desea verificar la complejidad en el tiempo de la funcion? (si/no): ")
        if verificarComplejidad.lower() == "si":
            print(best)
        
        repetirProceso = input("Repetir proceso? (si/no): ")
        # pregunto si quiere volver a usar el programa
        if repetirProceso.lower() != "si":
            print("********** FIN DEL PROGRAMA **********")
            # detengo el bucle por completo
            break