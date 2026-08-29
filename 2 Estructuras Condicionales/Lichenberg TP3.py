#Ejercicio 1
print("\t----------EJERCICIO 1----------\n")

# Pedimos la edad al usuario
edadUsuario = int(input("Ingrese su edad: "))

# Verificamos si es mayor o menor de edad
if edadUsuario >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")


#Ejercicio 2
print("\n\t----------EJERCICIO 2----------\n")

# Pedimos la nota del examen
nota = int(input("Ingrese su nota: "))

# Verificamos si esta aprobado o desaprobado (6 o mas aprueba)
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")


#Ejercicio 3
print("\n\t----------EJERCICIO 3----------\n")

# Bucle while que se repite hasta que el usuario ingrese un numero par
while True:
    numero = int(input("Ingrese un numero par: "))
    if numero % 2 == 0:
        print("Ha ingresado un numero par")
        break
    else:
        print("Por favor, ingrese un número par")


#Ejercicio 4
print("\n\t----------EJERCICIO 4----------\n")

# Pedimos la edad para clasificar la etapa de la vida
edad = int(input("Ingrese su edad: "))

# Evaluamos los rangos de edad
if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a Joven")
else:
    print("Adulto/a")


#Ejercicio 5
print("\n\t----------EJERCICIO 5----------\n")

# Bucle while para validar que la contraseña tenga entre 8 y 14 caracteres
while True:
    contraseña = input("Ingrese su contraseña de entre 8 y 14 caracteres: ")
    if len(contraseña) >= 8 and len(contraseña) <= 14:
        print("Ha ingresado una contraseña correcta")
        break
    else:
        print("Ingrese una contraseña de entre 8 y 14 caracteres")


#Ejercicio 6
print("\n\t----------EJERCICIO 6----------\n")

from statistics import mode, median, mean
import random

# Generamos 50 numeros aleatorios del 1 al 100
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calculamos la moda, la mediana y la media
try:
    moda = mode(numeros_aleatorios)
except:
    moda = numeros_aleatorios[0]

mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

print("Numeros generados:", numeros_aleatorios)
print(f"Media: {media:.2f} | Mediana: {mediana} | Moda: {moda}")

# Evaluamos si tiene sesgo positivo, negativo o sin sesgo
if media > mediana and mediana > moda:
    print("Sesgo Positivo")
elif media < mediana and mediana < moda:
    print("Sesgo Negativo")
else:
    print("Sin sesgo")


#Ejercicio 7
print("\n\t----------EJERCICIO 7----------\n")

# Pedimos una frase o palabra
frase = input("Ingrese una frase o palabra: ")

# Verificamos si la ultima letra es una vocal
if frase and frase[-1].lower() in ["a", "e", "i", "o", "u"]:
    print(f"{frase}!")
else:
    print(frase)


#Ejercicio 8
print("\n\t----------EJERCICIO 8----------\n")

# Pedimos el nombre y la opcion que desea
nombre = input("Ingrese su nombre: ")
numero = input("Opcion 1: Mayusculas \n Opcion 2: Minusculas \n Opcion 3: Solo primera mayuscula \nIngrese una opcion: ")

# Usamos match case para aplicar el formato seleccionado
match numero:
    case "1":
        resultado = nombre.upper()
        print(resultado)
    case "2":
        resultado = nombre.lower()
        print(resultado)
    case "3":
        resultado = nombre.title()
        print(resultado)
    case _:
        print("Opcion no valida")


#Ejercicio 9
print("\n\t----------EJERCICIO 9----------\n")

# Pedimos la magnitud del terremoto
terremoto = float(input("Ingrese la magnitud del terremoto: "))

# Evaluamos la escala de magnitud
if terremoto < 3:
    print("Muy leve")
elif terremoto >= 3 and terremoto < 4:
    print("Leve")
elif terremoto >= 4 and terremoto < 5:
    print("Moderado")
elif terremoto >= 5 and terremoto < 6:
    print("Fuerte")
elif terremoto >= 6 and terremoto < 7:
    print("Muy Fuerte")
else:
    print("Extremo")


#Ejercicio 10
print("\n\t----------EJERCICIO 10----------\n")

# Pedimos los datos del hemisferio, mes y dia
hemisferio = input("¿En qué hemisferio estás? (N/S): ").upper()
mes = int(input("¿Qué mes es? (1-12): "))
dia = int(input("¿Qué día es? (1-31): "))

# Evaluamos la estacion segun la fecha y el hemisferio
if hemisferio == "N":
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        estacion = "Verano"
    else:
        estacion = "Otoño"
else:
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        estacion = "Invierno"
    else:
        estacion = "Primavera"

print("La estación es:", estacion)
