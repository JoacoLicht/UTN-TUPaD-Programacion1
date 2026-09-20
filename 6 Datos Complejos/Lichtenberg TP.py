print("\t----------EJERCICIO 1----------\n")

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':1450}

precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

print(precios_frutas)

print("\t----------EJERCICIO 2----------\n")

precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

print(precios_frutas)

print("\t----------EJERCICIO 3----------\n")

lista_frutas = list(precios_frutas.keys())

print(lista_frutas)

print("\t----------EJERCICIO 4----------\n")

contactos={}

for i in range (5):
    nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
    numero = int(input(f"Ingrese el telefono de {nombre}: "))
    contactos[nombre] = numero

busqueda = input("\nIngrese el nombre a consultar: ")

if busqueda in contactos:
    print(f"El telefono de {busqueda} es: {contactos[busqueda]}")
else:
    print("Contacto no encontrado")

print("\t----------EJERCICIO 5----------\n")

frase= input("Ingrese una frase: ")

palabras= frase.lower().split() #creamos una lista con el metodo split, y le aplicamos lower para que si hay un HOLA y hola los tome como repetido
palabras_unicas = set(palabras) #pasa la lista a set, que filtra los repetidos

print ("\n---Palabras Unicas---")
print(palabras_unicas) #mostramos las palabras unicas

frecuencia = {} #creamos un diccionario

for palabra in palabras:
    frecuencia[palabra] = frecuencia.get(palabra,0)+1 #Busca el conteo actual de la palabra en el diccionario; si no la ha contado antes, devuelve 0 como valor inicial y le suma 1.

print("\n---Frecuencia de Palabras---")
print(frecuencia)

print("\t----------EJERCICIO 6----------\n")

def ingresar_nota(mensaje):
    """Solicita una nota al usuario y valida que sea un número entre 0 y 10."""
    while True:
        try:
            nota = float(input(mensaje))
            if 0 <= nota <= 10:
                return nota
            else:
                print(" Error: La nota debe estar entre 0 y 10.")
        except ValueError:
            print(" Error: Entrada inválida. Por favor, ingresa un número.")

# Diccionario para almacenar los datos
alumnos = {}

print("--- REGISTRO DE ALUMNOS Y NOTAS ---\n")

# Cargar datos de 3 alumnos
for i in range(1, 4):
    nombre = input(f"Ingresa el nombre del alumno {i}: ").strip().capitalize() #.strip() quita los espacios como el ENTER dado sin querer .capitalize() La primera letra la pone en mayusculas
    
    print(f"Ingresando notas para {nombre}:")
    nota1 = ingresar_nota("  Nota 1: ")
    nota2 = ingresar_nota("  Nota 2: ")
    nota3 = ingresar_nota("  Nota 3: ")
    
    # Guardamos las 3 notas juntas dentro de una Tupla
    notas_tupla = (nota1, nota2, nota3)
    
    # Guardamos la tupla en el diccionario usando el nombre como clave
    alumnos[nombre] = notas_tupla
    print()

# Mostrar promedios
print("--- RESULTADOS Y PROMEDIOS ---")
for nombre, notas in alumnos.items():
    # sum(notas) suma los 3 valores de la tupla
    promedio = sum(notas) / len(notas) # /3 tambien funciona, pero es buena practica usar el len
    print(f"• {nombre}: Notas {notas} | Promedio: {promedio:.2f}")

print("\t----------EJERCICIO 7----------\n")

# Definición de las listas de estudiantes que aprobaron
parcial1 = {"Ana", "Bruno", "Carlos", "Diana", "Esteban"}
parcial2 = {"Carlos", "Diana", "Facundo", "Gabriel"}

# 1. Aprobaron ambos parciales (Intersección)
ambos = parcial1 & parcial2
print("Aprobaron ambos parciales:", ambos)

# 2. Aprobaron solo uno de los dos (Diferencia simétrica)
solo_uno = parcial1 ^ parcial2
print("Aprobaron solo uno de los parciales:", solo_uno)

# 3. Lista total que aprobó al menos un parcial (Unión)
al_menos_uno = parcial1 | parcial2
print("Aprobaron al menos un parcial:", al_menos_uno)

print("\t----------EJERCICIO 8----------\n")

stock = {
    "Manzana": 50,
    "Banana": 30,
    "Naranja": 20
}

# Solicitamos el nombre del producto y normalizamos
producto = input("Ingresa el nombre del producto: ").strip().capitalize()

# Verificamos si el producto existe en el diccionario
if producto in stock:
    print(f" El producto '{producto}' existe. Stock actual: {stock[producto]}")
    
    # Preguntamos si desea agregar unidades
    unidades = int(input("¿Cuántas unidades deseas agregar?: "))
    stock[producto] = stock[producto] + unidades
    print(f"Nuevo stock de {producto}: {stock[producto]}")

else:
    print(f" El producto '{producto}' no existe en el sistema.")
    
    # Agregamos el nuevo producto
    cantidad_inicial = int(input(f"Ingresa el stock inicial para {producto}: "))
    stock[producto] = cantidad_inicial
    print(f"Producto '{producto}' agregado con un stock de {cantidad_inicial}.")

print("\n--- STOCK ACTUALIZADO ---")
print(stock)

print("\t----------EJERCICIO 9----------\n")

agenda = {
    ("Lunes", "10:00"): "Reunión de equipo",
    ("Lunes", "15:00"): "Clase de Python",
    ("Miércoles", "09:00"): "Cita médica",
    ("Viernes", "18:00"): "Gimnasio"
}

print("--- CONSULTA DE AGENDA ---")
dia = input("Ingresa el día (ej: Lunes): ").strip().capitalize()
hora = input("Ingresa la hora (ej: 10:00): ").strip()

# Creamos la tupla de búsqueda con las entradas del usuario
clave_busqueda = (dia, hora)

# Buscamos en el diccionario usando .get() para evitar errores si no hay evento
evento = agenda.get(clave_busqueda, "No hay ningún evento registrado en esa fecha y hora.")

print(f"\nResultado para {dia} a las {hora}:")
print("->", evento)

print("\t----------EJERCICIO 10----------\n")

paises_capitales = {
    "Argentina": "Buenos Aires",
    "España": "Madrid",
    "Francia": "París",
    "Italia": "Roma"
}

# Diccionario donde guardaremos el resultado invertido
capitales_paises = {}

# Recorremos el diccionario original con .items()
for pais, capital in paises_capitales.items():
    # Asignamos la capital como nueva clave y el país como nuevo valor
    capitales_paises[capital] = pais

print("Diccionario original (País -> Capital):")
print(paises_capitales)

print("\nDiccionario invertido (Capital -> País):")
print(capitales_paises)