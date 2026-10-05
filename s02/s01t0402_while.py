"""
Escribir un programa que calcule
la suma de los "n" numeros naturales,
Por ejemplo si no = 100, el programa 
calculara la suma del 1 al 100
42
"""

# Importamos biblioteca time
import time

#Crear las variables para el problema
n = 100
the_sum = 0

#Tomando el tiempo 1
timestamp_01 = time.time()

#Iniciando la suma
#100
while(n > 0):
    the_sum = the_sum + n #100 + 99 + 98 + ... + 1
    n = n - 1

#Tomamos el tiempo 2
timestamp_02 = time.time()

#Imprimir solución
print(f"La suma es: {the_sum}")

#Calcular el time
elapsed_time = round((timestamp_02-timestamp_01) * 1e6, 2)
print(f"Tiempo de ejecucución: {elapsed_time} us")

