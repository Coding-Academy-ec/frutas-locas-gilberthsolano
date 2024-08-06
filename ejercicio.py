# ejercicio.py

# Crea un diccionario llamado "frutas" con las siguientes parejas clave-valor:
# "manzana" - "roja"
# "banana" - "amarilla"
# "pera" - "verde"
# "naranja" - "naranja"

frutas = {
    "manzana": "roja",
    "banana": "amarilla",  # banana lleva el valor "amarilla"
    "pera": "verde",
    "naranja": "naranja"   # naranja lleva el valor "naranja"
}

# Imprime el diccionario "frutas" en la consola.
print(frutas)

# Imprime el valor asociado a la clave "banana" en la consola.
print(frutas["banana"])  # banana lleva el valor "amarilla"

# Imprime el valor asociado a la clave "uva" en la consola.
print(frutas.get("uva"))  # Esto imprimirá 'None' ya que "uva" no está en el diccionario
