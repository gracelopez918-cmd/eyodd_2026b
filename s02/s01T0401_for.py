"""
Escribir un programa que calcule
la suma de los "n" numeros naturales,
Por ejemplo si no = 100, el programa 
calculara la suma del 1 al 100
42
"""

# Importamos biblioteca time
import time

#Tomando el tiempo inicial 
timestamp_01 = time.time()

#Progrma que calcula la suma
# de los "n" numeros naturales
n = 100
total_sum = 0

# Ciclo for para la suma
for number in range(1,n+1):
    total_sum = total_sum + number
    #1: sum <- 0 + 1
    #sum = 1
    #2: suma <- 1 + 2
    #sum = 3
    #3: suma <- 1 + 3
    #sum = 4
    #...
    #100: sum <- antSum + 100
print(f"la suma de 1 hasta {n} es: {total_sum}")

#Tomando el timepo final 
timestamp_02 = time.time()

#Impresión del tiempo de ejecución 
print(f"Tiempo de ejecución: {(timestamp_02-timestamp_01) * 1e6:.2f} μs")