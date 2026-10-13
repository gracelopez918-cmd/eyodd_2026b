# Importando el modulo Arrays
import array as arr

# Creando un arreglo
# i: Entero con signo
# I: Enteto sin signo
# f: Numero decimal
# d: Numero decimal doble
# u: Caracter unico
my_array = arr.array('i',[10,22,300,3,7,40,11,17,222,777,67])

# Iterando automaticamente
# for num in my_array:
#     # print(num)

# Acceso individual a cada elemneto
# print(my_array[0]) #Primer elemento
# print(my_array[1]) #Segundo elemento
# print(my_array[1]) #Tercer elemento

#Tamaño de un arreglo
#length
# print(len(my_array))

# Iteración indices
# for i in range(len(my_array)):
#     if my_array[i] % 2 == 0:
#         print(f"Elemento Num {i+1}:{my_array[i]}")

#Busqueda de un elemento
num_to_search = 200

# Modificando un valor
# backet notacion
my_array[7]=200 

try:
    print(f"Localizando {num_to_search}: {my_array.index(num_to_search)}")
except:
    print("⚠️ Numero no encontrado!!!")

