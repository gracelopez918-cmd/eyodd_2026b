# Importamos array de la biblioteca y lo renombramos como arr
from array import array as arr

# Parametros de mi matricula
rows = 8
columns = 2 * rows - 1

# Creando la reticula 2D
matrix = []
# Construyendo el grid/rejilla
for _ in range(rows):
    new_row = arr('i', [0] * columns)
    matrix.append(new_row)

# Validando la construcción del Grid
print(f"Cantidad de filas: {len(matrix)}")
print(f"Cantidad de columnas: {len(matrix[0])}")

for row in matrix:
    print(list(row))