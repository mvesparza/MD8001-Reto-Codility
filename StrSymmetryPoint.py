"""
Programa que encuentra un punto de simetría de una cadena, si lo hay.

Autor: Marco Vinicio Esparza

Versión: v2.3
"""

import big_o

def solucion(S):
    """
    Proceso que verifica la simetría de las subcadenas de la cadena ingresada
    Parámetros:
    --------------
    Si, recibe un parámetro S que es una palabra.

    Retorna:
    --------------
    Si, retorna la cantidad de caracteres simétricos de la palabra y -1 si
    la palabra no es simétrica. 
    """
    for i in range(len(S)):
        if S[:i] == S[i+1:][::-1]:
            return i
    return ("La palabra no es simétrica", -1)

if __name__ == '__main__':
    # inicializo el programa
    print("********* Encuentra un punto de simetría de una cadena, si lo hay *********")
    # inicio bucle para repetir el proceso las veces que el usuario quiera
    while(True):
        # declaro una variable global
        S = input("Ingrese una palabra simétrica : ")
        resultado = solucion(S)
        print("Las subcadenas son de índice: ", resultado)

        # Variable para calcular la complejidad
        num = lambda n: S
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