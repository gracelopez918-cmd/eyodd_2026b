# Importamos array del modulo array y renombrado arr
from array import array as arr

# Importando una funcion de otro archivo
from s02t0102_1d import print_array

my_array = arr('i',[2,10,15,20])
print("--- ANTES DE LA INSERCIÓN--.")
print_array(my_array)

# Inserción
my_array.insert(1,90)
print("--- DESPUES DE LA INSERCIÓN--.")
print_array(my_array)

my_array.append(100)
print("--- DESPUES DE UN APPEND--.")
print_array(my_array)

print("--- SIMULADOR DE UN APPEND CON UN INSERT--.")
my_array.insert(len(my_array),90000)
print_array(my_array)
