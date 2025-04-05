# Creamos un archivo denominado "my_notes.txt"
file_name = "my_notes.txt"

# Modo de apertura: "w" para escritura (write)
archivo_escritura = open(file_name, "w")

# Escribimos 3 notas personales, usando el método write()
archivo_escritura.write("Línea 1: Estudiar para los exámenes finales.\n")
archivo_escritura.write("Línea 2: Ir a cortarme el pelo.\n")
archivo_escritura.write("Línea 3: Entregar todas las tareas a tiempo.\n")

# Cerramos el archivo de escritura
archivo_escritura.close()

# Modo de apertura: "r" para lectura (read)
archivo_lectura = open(file_name, "r")

# Leemos y mostramos el contenido para verificar
contenido = archivo_lectura.read()
print("Contenido del archivo después de escribir:")
print(contenido)

# Cerramos el archivo de lectura
archivo_lectura.close()