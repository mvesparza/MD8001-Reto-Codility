"""
Programa que dadas dos cadenas que representan los tiempos de entrada y salida de un estacionamiento
de automóviles, encuentra el costo del boleto de acuerdo con las reglas de facturación dadas.

Autor: Marco Vinicio Esparza

Versión: v2.1
"""

import big_o

def solution(E, L):
    """
    Proceso que calcula el costo del boleto del estacionamiento dado la hora de entrada y salida
    Parámetros:
    --------------
    Si, recibe un parámetro E y L.
    E: las horas y minutos de entrada.
    L: las horas y minutos de salida.
    Retorna:
    --------------
    Si, retorna el costo del boleto.
    
    """
    # Convertir hora de entrada y salida en minutos
    entrada = int(E[:2]) * 60 + int(E[3:])
    salida = int(L[:2]) * 60 + int(L[3:])
    # Calcular la diferencia en minutos
    diferencia = salida - entrada
    # Calcular el costo del boleto
    costo = 2 + 3
    if diferencia > 60:
        costo += (4 * ((diferencia // 60) - 1))
    if diferencia % 60 != 0:
        costo += 4
    return costo

if __name__ == '__main__':
    # inicializo el programa
    print("********* Costo tiempo de parqueo *********")
    # inicio bucle para repetir el proceso las veces que el usuario quiera
    while(True):
        E =  input("Ingresa la hora de entrada en el formato HH:MM: ")
        L =  input("Ingresa la hora de salida en el formato HH:MM: ")
        print("El costo del ticket es:", solution(E, L), "$")
        
        # Variables para calcular la complejidad
        num = lambda n: E
        num1 = lambda j: L
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