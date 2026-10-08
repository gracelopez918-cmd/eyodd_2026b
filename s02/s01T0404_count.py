# Creamos una lista de estudiantes
student_list_01 = ['Jordan','Pipen','Curry','Shack'] # O(1) 

def random_function(students):
    first = students[0] # O(1)
    total = 0            # O(1)
    new_list = []        # O(1)

    for student in students:  
        print("Se le suma 1 a total")
        total += 1                 # O(n) 
        new_list.append(student)   # O(n) 

    print(new_list)        # O(1)
    return total           # O(1)

print(f"Tamaño de lista: {len(student_list_01)}")
print(random_function(student_list_01))
print("")

# Calcular O(?) 
# O(1) + O(1) + O(1) + O(n) + O(n) + O(1) + O(1)
#= O(1 + 1 + 1 + n + n + 1 + 1)
#= O(5 + 2n)
#Complejidad de = O(n)



"""
Si hay un for su complejidad es O(n)
si hay un for y desntro de este otro for es O(n^2)
"""