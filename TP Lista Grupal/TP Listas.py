# TP Listas de una dimensión — Resolución

## Ejercicio 1: Suma de elementos
numeros = input("Ingrese números separados por espacios: ").split()

numeros = [int(numero) for numero in numeros]

suma = sum(numeros)

print("La suma es:", suma)

## Ejercicio 2: Encontrar el mayor y el menor


numeros = input("Ingrese números separados por espacios: ").split()

numeros = [int(numero) for numero in numeros]

mayor = max(numeros)
menor = min(numeros)

print("El mayor es:", mayor)
print("El menor es:", menor)

## Ejercicio 3: Invertir una lista

lista = input("Ingrese elementos separados por espacios: ").split()

lista_invertida = lista[::-1]

print("Lista original:", lista)
print("Lista invertida:", lista_invertida)

## Ejercicio 4: Contar elementos pares e impares

numeros = input("Ingrese números separados por espacios: ").split()

numeros = [int(numero) for numero in numeros]

pares = 0
impares = 0

for numero in numeros:
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Cantidad de pares:", pares)
print("Cantidad de impares:", impares)


## Ejercicio 5: Multiplicar elementos por un valor

numeros = input("Ingrese números separados por espacios: ").split()

numeros = [int(numero) for numero in numeros]

valor = int(input("Ingrese el valor por el que quiere multiplicar: "))

resultado = []

for numero in numeros:
    resultado.append(numero * valor)

print("Resultado:", resultado)

## Ejercicio 6: Eliminar duplicados

numeros = input("Ingrese números separados por espacios: ").split()

numeros = [int(numero) for numero in numeros]

sin_duplicados = list(set(numeros))

print("Lista sin duplicados:", sin_duplicados)

## Ejercicio 7: Promedio de una lista

numeros = input("Ingrese números separados por espacios: ").split()

numeros = [int(numero) for numero in numeros]

promedio = sum(numeros) / len(numeros)

print("El promedio es:", promedio)

## Ejercicio 8: Encontrar elementos repetidos


numeros = input("Ingrese números separados por espacios: ").split()
numeros = [int(numero) for numero in numeros]

diccionario = {}

for numero in numeros:
    if numero in diccionario:
        diccionario[numero] += 1
    else:
        diccionario[numero] = 1

repetidos = []

for numero in diccionario:
    if diccionario[numero] > 1:
        repetidos.append(numero)

print("Elementos repetidos:", repetidos)

## Ejercicio 9: Lista de números primos

def es_primo(numero):
    if numero < 2:
        return False

    for i in range(2, numero):
        if numero % i == 0:
            return False

    return True


numeros = input("Ingrese números separados por espacios: ").split()

numeros = [int(numero) for numero in numeros]

primos = []

for numero in numeros:
    if es_primo(numero):
        primos.append(numero)

print("Números primos:", primos)

## Ejercicio 10: Eliminar un elemento por su índice

numeros = input("Ingrese números separados por espacios: ").split()

numeros = [int(numero) for numero in numeros]

indice = int(input("Ingrese el índice que desea eliminar: "))

if 0 <= indice < len(numeros):
    del numeros[indice]
    print("Lista resultante:", numeros)
else:
    print("El índice no existe.")


## Ejercicio 11: Contar ocurrencias de un elemento

numeros = input("Ingrese números separados por espacios: ").split()

numeros = [int(numero) for numero in numeros]

numero_buscado = int(input("Ingrese el número que desea buscar: "))

cantidad = numeros.count(numero_buscado)

print("El número aparece", cantidad, "veces.")


## Ejercicio 12: Sumar listas elemento por elemento

lista1 = input("Ingrese la primera lista: ").split()
lista2 = input("Ingrese la segunda lista: ").split()

lista1 = [int(numero) for numero in lista1]
lista2 = [int(numero) for numero in lista2]

if len(lista1) == len(lista2):
    resultado = []

    for i in range(len(lista1)):
        resultado.append(lista1[i] + lista2[i])

    print("Resultado:", resultado)
else:
    print("Las listas deben tener la misma longitud.")

## Ejercicio 13: Numpy

print("NumPy es una librería de Python que permite trabajar de manera más eficiente con arrays y matrices.")
#Ejemplo:

#import numpy as np

#matriz = np.array([
#    [1, 2, 3],
#    [4, 5, 6],
#    [7, 8, 9]
#])
#print(matriz)
#print("NumPy permite realizar operaciones matemáticas con matrices de manera sencilla y eficiente.")
#Ejemplo
#print(np.sum(matriz))


# TP Listas Bidimensionales — Resolución

## Ejercicio 1: Crear una matriz de números

def crear_matriz(filas, columnas):
    matriz = []
    numero = 1

    for i in range(filas):
        fila = []

        for j in range(columnas):
            fila.append(numero)
            numero += 1

        matriz.append(fila)

    return matriz


filas = int(input("Ingrese cantidad de filas: "))
columnas = int(input("Ingrese cantidad de columnas: "))

matriz = crear_matriz(filas, columnas)

for fila in matriz:
    print(fila)

## Ejercicio 2: Suma de todos los elementos

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

suma = 0

for fila in matriz:
    suma += sum(fila)

print("La suma total es:", suma)

## Ejercicio 3: Suma de cada fila

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i, fila in enumerate(matriz):
    print("Suma de la fila", i + 1, ":", sum(fila))

## Ejercicio 4: Matriz transpuesta

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transpuesta = []

for columna in range(len(matriz[0])):
    fila = []

    for fila_original in range(len(matriz)):
        fila.append(matriz[fila_original][columna])

    transpuesta.append(fila)

print("Matriz original:")

for fila in matriz:
    print(fila)

print("Matriz transpuesta:")

for fila in transpuesta:
    print(fila)

## Ejercicio 5: Encontrar el elemento mayor

matriz = [
    [10, 25, 3],
    [45, 8, 12],
    [7, 30, 18]
]

mayor = matriz[0][0]

for fila in matriz:
    for elemento in fila:
        if elemento > mayor:
            mayor = elemento

print("El elemento mayor es:", mayor)

## Ejercicio 6: Multiplicar una matriz por un escalar

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

escalar = int(input("Ingrese el valor escalar: "))

resultado = []

for fila in matriz:
    nueva_fila = []

    for elemento in fila:
        nueva_fila.append(elemento * escalar)

    resultado.append(nueva_fila)

print("Matriz resultante:")

for fila in resultado:
    print(fila)

## Ejercicio 7: Diagonal de una matriz cuadrada

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

diagonal = []

for i in range(len(matriz)):
    diagonal.append(matriz[i][i])

print("Diagonal principal:", diagonal)

## Ejercicio 8: Matriz identidad

n = int(input("Ingrese el tamaño de la matriz: "))

matriz = []

for i in range(n):
    fila = []

    for j in range(n):
        if i == j:
            fila.append(1)
        else:
            fila.append(0)

    matriz.append(fila)

for fila in matriz:
    print(fila)

## Ejercicio 9: Matriz identidad inversa

n = int(input("Ingrese el tamaño de la matriz: "))

matriz = []

for i in range(n):
    fila = []

    for j in range(n):
        if i + j == n - 1:
            fila.append(1)
        else:
            fila.append(0)

    matriz.append(fila)

for fila in matriz:
    print(fila)

## Ejercicio 10: Verificar matriz simétrica

matriz = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
]

simetrica = True

for i in range(len(matriz)):
    for j in range(len(matriz)):
        if matriz[i][j] != matriz[j][i]:
            simetrica = False

if simetrica:
    print("La matriz es simétrica.")
else:
    print("La matriz no es simétrica.")

## Ejercicio 11: Rotar una matriz 90 grados

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotada = []

for j in range(len(matriz[0])):
    fila = []

    for i in range(len(matriz) - 1, -1, -1):
        fila.append(matriz[i][j])

    rotada.append(fila)

print("Matriz rotada 90 grados:")

for fila in rotada:
    print(fila)

## Ejercicio 12: Analizador y filtrado de calificaciones

notas_texto = "45, 88, -5, 92, 30, 110, 75, 60, 15"

notas = notas_texto.split(",")

aprobados = []
reprobados = []

for nota in notas:
    nota = int(nota.strip())

    if nota < 0 or nota > 100:
        continue

    if nota >= 60:
        aprobados.append(nota)
    else:
        reprobados.append(nota)

notas_validas = aprobados + reprobados

promedio = sum(notas_validas) / len(notas_validas)

print("Aprobados:", aprobados)
print("Reprobados:", reprobados)
print("Promedio de notas válidas:", promedio)
print("Últimos 2 aprobados:", aprobados[-2:])

## Ejercicio 13: Gestor interactivo de proyectos

tareas = []

while True:

    print("\n--- MENÚ ---")
    print("1. Agregar tarea")
    print("2. Eliminar tarea")
    print("3. Ver resumen")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        tarea = input("Ingrese el nombre de la tarea: ")

        if tarea in tareas:
            print("La tarea ya está registrada.")
        else:
            tareas.append(tarea)
            print("Tarea agregada correctamente.")

    elif opcion == "2":

        tarea = input("Ingrese la tarea que desea eliminar: ")

        if tarea in tareas:
            tareas.remove(tarea)
            print("Tarea eliminada correctamente.")
        else:
            print("La tarea no existe.")

    elif opcion == "3":

        print("Total de tareas:", len(tareas))
        print("Primeras 3 tareas:", tareas[:3])

    elif opcion == "4":

        print("Programa finalizado.")
        break

    else:
        print("Opción no válida.")
