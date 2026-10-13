"""
Escribir un programa que calcule
la suma de los "n" numeros naturales,
Por ejemplo si no = 100, el programa 
calculara la suma del 1 al 100
42
"""

# Importamos biblioteca time/Tiempo
import time

# Variable para guardar el data set
dataset = []

# Repetir para n = 500, 1000, 1500, 2000, ... 5000
for repetition in range(1, 11):

    #Crear las variables para el problema
    n = repetition * 500
    the_sum = 0

    #Tomando el tiempo 1
    timestamp_01 = time.time()

    #Iniciando la suma
    while(n > 0):
        the_sum = the_sum + n
        n = n - 1

    #Tomamos el tiempo 2
    timestamp_02 = time.time()

    #Calcular el time
    elapsed_time = round((timestamp_02-timestamp_01) * 1e6, 2)

    # Agregar los datos al dataset
    dataset.append((repetition * 500, elapsed_time, the_sum))

# Imprimir el dataset
for tup in dataset:
    print(tup)