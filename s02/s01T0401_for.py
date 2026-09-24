"""
Escribir un programa que calcule
la suma de los "n" numeros naturales,
Por ejemplo si no = 100, el programa 
calculara la suma del 1 al 100
42
"""

# Importamos biblioteca time
import time

#Funcion que suma los primeros "n" numeros naturales
def sum_of_n(n):
    total_sum = 0
    #Sumando los "n" números
    #Ciclo for
    for number in range(1,n+1):
        total_sum = total_sum + number
    #Retornando el total de la suma
    return total_sum

#Variable para guardar el data set
dataset = [] #((n, time))

#Como guardar el contenido del dataset
for repetition in range(1,11):
    #⏱️Tomando el tiempo inicial 
    timestamp_01 = time.time()

    #Sumo los "n" numeros
    n = repetition*500
    #Guardo mi resultado en result
    result = sum_of_n(n)

    #⏱️Tomando el timepo final 
    timestamp_02 = time.time()

    #Impresión del tiempo de ejecución
    elapsed_time = round((timestamp_02-timestamp_01) * 1e6,2)

    #Agregar la tripreta de los datos a dataset
    dataset.append((n,elapsed_time,result))

#
for tup in dataset:
    print(tup)