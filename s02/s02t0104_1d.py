# Eliminación
# Importamos array del modulo array y renombrado arr
from array import array as arr

# Importando una funcion de otro archivo
from s02t0102_1d import print_array

my_array = arr('i',[2,10,15,20,10])

print("--- ANTES DE LA ELIMINACIÓN--.")
print_array(my_array)

# Eliminacion
try:
    my_array.remove(10)
except:
    print("⚠️ Numero no encontrado en el arreglo!!!")
print("--- DESPUES DE LA ELEMINACIÓN--.")
print_array(my_array)

