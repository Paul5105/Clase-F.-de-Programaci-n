#Matriz bidimensional (3x3)
matriz=[
    [7, 3, 8],
    [6, 9, 1],
    [5, 2, 4]
]
print(matriz[2][0])
#Búsqueda en la matriz para encontrar un valor en específico
valor_a_buscar = 4

for fila in range(len(matriz)):
    for columna in range(len(matriz[fila])):
        if matriz[fila][columna] == valor_a_buscar:
            print(f"Encuentro la posición ({fila}, {columna})")
            break
    else:
        continue # siguiente
    break
else:
    print("Valor no encontrado")


