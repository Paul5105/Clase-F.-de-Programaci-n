#   Creamos un diccionario el cual llamaremos "Información personal"
informacion_personal = {"Nombre":"Ricardo", "Edad":"32", "Ciudad":"Azogues", "Profesión":"Arquitecto"}
print(informacion_personal)
#Accedemos
print(informacion_personal["Edad"])
print(informacion_personal["Ciudad"])
#Accedemos al valor asociado con la clave "ciudad" y modifícamos con una ciudad diferente.
informacion_personal["Ciudad"] = "Cuenca"
print(informacion_personal)
#Agregamos una nueva clase valor que representa la profesión.
informacion_personal["Profesión"] = "Ingeniero"
print(informacion_personal)
#Verifica si la clave "telefono" existe en el diccionario. Si no existe, agrégala con un número de teléfono ficticio.
#Como no existe la clave "telefono" procedo a agregarla.
if "Telefono" not in informacion_personal:
    informacion_personal["Telefono"] = "8567767346"
#Eliminamos la clave "Edad" del diccionario.
del informacion_personal["Edad"]
print(informacion_personal)
#Gracias