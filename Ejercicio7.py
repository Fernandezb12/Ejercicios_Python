#Programa que solicite al usuario los datos para calcular el área de un Círculo (●), 
#finalmente mostrar el resultado en pantalla.

import math

radio = float(input("Introduce el radio del círculo: "))

areaC = math.pi * radio**2

print("El área del círculo es: ", + areaC)