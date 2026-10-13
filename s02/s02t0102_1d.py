# Importando el modulo Array 
# de la biblioteca array y renombrado como arr
from array import array as arr

def print_array(input):
    print("[",end="")
    for element in input:
        print(element, end=',')
    print("\b]")

my_arrey = arr('i', [5,10,15,20])
print_array(my_arrey)

#Buscar el elemento 15
number_to_search = 100
counter = 0
print(f"Se busca {number_to_search} en el arreglo")
for integer in my_arrey:
    if integer == number_to_search:
        print("🎉Numero encontrado")
    #Sirve para terminar el ciclo
    break
# Incrementar counter
    counter+=1
    if counter == len(my_arrey):
        print("⛔Numero no encontrado")