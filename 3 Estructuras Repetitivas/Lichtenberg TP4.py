#Ejercicio 1

print("\t----------EJERCICIO 1----------\n")

#Hacemos un bucle for hasta el rango 101
for i in range(101):
    print(i)

#Ejercicio 2
print("\n\t----------EJERCICIO 2----------\n")
numero = int(input("Ingrese un número entero: "))

# Si el número es negativo, lo convertimos a positivo
numero = abs(numero)

contador = 0

# Caso especial para el 0
if numero == 0:
    contador = 1
else:
    while numero > 0:
        numero = numero // 10   # Elimina el último dígito
        contador += 1

print("La cantidad de dígitos es: ",contador)

#Ejercicio 3
print("\n\t----------EJERCICIO 3----------\n")
#Ingreso de numeros
nro1 = int(input("Ingrese el primer numero: "))
nro2 = int(input("Ingrese el segundo numero: "))
sumaTotal = 0
if nro1 == nro2: #Si el numero es igual a 0, la suma entre los dos tambien
    sumaTotal = 0
else:
    if nro1 > nro2: #Si el nro1 es mayor al nro2, se suman los numeros entre nro2 y nro1 respectivamente
        while nro1 - 1 != nro2:
            nro2 += 1
            sumaTotal += nro2
    else:
        while nro1 != nro2 - 1: #Se calcula el caso contrario, nro2 mayor que nro1
                    nro1 += 1
                    sumaTotal += nro1

print(f"La suma total es {sumaTotal}")

#Ejercicio 4
print("\n\t----------EJERCICIO 4----------\n")
num =int(input("Ingrese un numero: ")) #Pedimos al usuario un numero
totalsuma= 0 #iniciamos en sero el total de la suma

while  num != 0: #creamos un bucle while que sea distinto de 0
    totalsuma += num #contador
    num =int(input("Ingrese otro numero: "))

print("La suma total de los numero es: ",totalsuma)#ponemos la suma total

#Ejercicio 5
print("\n\t----------EJERCICIO 5----------\n")
import random
aleatorio = random.randint(0,9) #Se calcula el numero aleatorio entre 0 y 9
acertado=int(input("Ingrese el numero que cree que va a salir del 0 al 9: "))
intentos = 1
while aleatorio!= acertado: #Mientras el numero ingresado sea distinto de el numero a adivinar
    intentos += 1
    acertado=int(input("Ingrese otro numero del 0 al 9: "))
print(f"¡Ganaste!, Has intentado {intentos} veces\n El numero era {aleatorio}")

#Ejercicio 6
print("\n\t----------EJERCICIO 6----------\n")

for i in range(100, -1, -2): #creamos un bucle for con el 100 y el 0 incluido
     print(i) # mostramos todos los pares de 100 a 0

#Ejercicio 7
print("\n\t----------EJERCICIO 7----------\n")
suma_numeros = 0
usuario=int(input("Ingrese un numero positivo: "))
usuario = abs(usuario) #Se obliga a calcular el positivo para evitar errores

for i in range(0, usuario + 1): #Itera desde 0 hasta el numero elegido incluido
     suma_numeros += i #Se calcula la suma de los numeros
print("La suma total de los numeros comprendidos son: ",suma_numeros)

#Ejercicio 8
print("\n\t----------EJERCICIO 8----------\n")

cantinumero= 100  #Iiniciamos la cantidad de numeros que pide el ejercicio
cant_positivo = 0
cant_negativo = 0 #Iniciamos las variables en 0
cant_impares = 0
cant_pares = 0
for i in range(0,cantinumero): # Creamos un bucle for que empiece de 0 a la cantidad de numeros
    numero = int(input(f"Ingrese el numero {i+1}: ")) #pedimos que ingrese un numero
    if numero % 2 != 0: #creamos un if con condiciones
        cant_impares +=1 #si es impar suma cuantos lleva
    else:
        cant_pares += 1 #si es par suma cuantos lleva
    if numero < 0:
        cant_negativo += 1 #si es negativo suma cuantos lleva
    else:
        cant_positivo +=1 #si es positivo suma cuantos lleva

print("Cantidad Positivos: ", cant_positivo)
print("Cantidad Negativos: ", cant_negativo)
print("Cantidad Impares: ", cant_impares)
print("Cantidad Pares: ",cant_pares)

#Ejercicio 9
print("\n\t----------EJERCICIO 9----------\n")
from statistics import mean #Importamos la funcion para calcular la media
cantinumero= 100
valores = list()
for i in range(0,cantinumero): 
    numero = int(input(f"Ingrese el numero {i+1}: "))
    valores.append(numero) #A cada numero ingresado, lo insertamos en una lista
print(f"La Media es: {mean(valores)}")  #Calculamos la media y mostramos en pantalla

#Ejercicio 10
print("\n\t----------EJERCICIO 10----------\n")
numero = int(input("Ingresa un número: "))

numero_invertido = 0
# Usamos un bucle para desarmar el número
while numero > 0:
    # 1. Obtenemos el último dígito con el residuo de la división por 10
    digito = numero % 10
    
    # 2. Lo agregamos al nuevo número invertido
    numero_invertido = (numero_invertido * 10) + digito
    
    # 3. Le quitamos el último dígito al número original
    numero = numero // 10

print("El número invertido es:", numero_invertido)