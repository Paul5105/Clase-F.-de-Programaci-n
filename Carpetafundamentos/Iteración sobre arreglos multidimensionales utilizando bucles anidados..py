# Creamos una matriz 3D
ciudades = ["Ciudad A", "Ciudad B", "Ciudad C"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
num_semanas = 4  # Número de semanas

# Crear una matriz 3D para almacenar las temperaturas
# Matriz[ciudad][semana][día] = temperatura
temperaturas = [
    [   # Ciudad A
        [25, 26, 27, 28, 29, 30, 31],  # Semana 1
        [24, 25, 26, 27, 28, 29, 30],  # Semana 2
        [23, 24, 25, 26, 27, 28, 29],  # Semana 3
        [22, 23, 24, 25, 26, 27, 28]   # Semana 4
    ],
    [   # Ciudad B
        [20, 21, 22, 23, 24, 25, 26],  # Semana 1
        [19, 20, 21, 22, 23, 24, 25],  # Semana 2
        [18, 19, 20, 21, 22, 23, 24],  # Semana 3
        [17, 18, 19, 20, 21, 22, 23]   # Semana 4
    ],
    [   # Ciudad C
        [15, 16, 17, 18, 19, 20, 21],  # Semana 1
        [14, 15, 16, 17, 18, 19, 20],  # Semana 2
        [13, 14, 15, 16, 17, 18, 19],  # Semana 3
        [12, 13, 14, 15, 16, 17, 18]   # Semana 4
    ]
]

# Seleccionar una ciudad en específico
ciudad_seleccionada = "Ciudad C"  # Cambia esto por la ciudad que desees(A,B,C)
ciudad_idx = ciudades.index(ciudad_seleccionada)  # Obtener el índice de la ciudad

# Mostrar el promedio de temperaturas para la ciudad seleccionada
print(f"Promedios de temperatura para {ciudad_seleccionada}:")
for semana_idx in range(num_semanas):
    # Obtener las temperaturas de la semana actual
    temps_semana = temperaturas[ciudad_idx][semana_idx]
    # Calcular el promedio
    promedio = sum(temps_semana) / len(temps_semana)
    # Mostrar el resultado
    print(f"  Semana {semana_idx + 1}: {promedio:.2f}°C")