"""
Escribir un programa que calcule
la suma de los "n" numeros naturales,
Por ejemplo si no = 100, el programa 
calculara la suma del 1 al 100
42
"""

# Importamos biblioteca time
import time

#Crear una marca de tiempo
timestamp_01 = time.time()

#Progrma que calcula la suma
# de los "n" numeros naturales
n = 100
sum = 0

# Ciclo for para la suma
for number in range(1,n+1):
    print(str(number) + " ")