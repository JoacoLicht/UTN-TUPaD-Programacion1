#Ejercicio 1 
print("Hola Mundo!") #mostramos por pantalla

#Ejercicio 2
nombre = input("Ingrese su nombre ") 
print(f"Hola {nombre}!") # hacemos un print que muestre su nombre

#Ejercicio 3
nombre = input("Ingrese su nombre: ") # le pedimos al usuario que ingrese su nombre,apellido,edad, y residencia
apellido= input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
lugarResidencia = input("Lugar de residencia :")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugarResidencia}.")  #juntamos todo en un solo print y lo muestra por pantalla

#Ejercicio 4
radio =float(input("Ingrese el radio: "))#ingresa un flotante
area= 3.14 * radio**2 #calculamos el area
perimetro = 2* 3.14 * radio #calculamos el perimetro
print(f"El area es: {area} y el perimetro es: {perimetro}") # mostramos por pantalla

#Ejercicio 5
segundos = int(input(" Ingrese los segundos: "))
hora = segundos / 3600 #calculamos la cuenta en horas
print(f" los segundos equivalen a {hora} horas") #mostramos por pantalla

#Ejercicio 6
numero =int(input("Dime un numero "))
print(f""" 
   {numero} x 0 = {numero * 0}
   {numero} x 1 = {numero * 1}
   {numero} x 2 = {numero * 2}
    {numero} x 3 = {numero * 3}
    {numero} x 4 = {numero * 4}
    {numero} x 5 = {numero * 5}
    {numero} x 6 = {numero * 6}
    {numero} x 7 = {numero * 7}
    {numero} x 8 = {numero * 8}
    {numero} x 9 = {numero * 9}
    {numero} x 10 = {numero * 10}
      """) #hacemos una tabla de multiplicar con el numero solicitado

#Ejercicio 7

numero1=int(input("Ingrese el primer numero distinto de 0: "))
numero2=int(input("Ingrese el segundo numero distinto de 0: ")) #pedimos al usuario que ingrese dos numeros distintos de 0

print(f"suma: {numero1 + numero2} division: {numero1/ numero2} multiplicacion: {numero1 * numero2} resta: {numero1 - numero2}") #hacemos las cuentas mientras mostramos por pantalla el resultado

#Ejercicio 8
altura = float(input("Ingrese su altura: ")) #pedimos al usuario su altura y peso
peso = float(input("Ingrese su peso: "))
imc= peso / altura**2 #sacamos el resultado de indice de masa corporal
print(f"su indice de masa corporal es: {imc}") #mostramos por pantalla

#Ejercicio 9
cel = int(input("Ingrese la temperatura de grados celsius: ")) #pedimos al usuario la temperatura en celsius
fahr= 9/5* cel + 32 #lo pasamos a grados fahrenheit
print(f"En grados Fahrenheit equivale a: {fahr}")#mostramos por pantalla

#Ejercicio 10
numero1= int(input("Ingrese el primer numero: "))
numero2= int(input("Ingrese el segundo numero: ")) #pedimos al usuario 3 numeros
numero3= int(input("Ingrese el tercer numero: "))

prom= (numero1 + numero2 + numero3) /3 #sacamos el promedio de dichos numeros
print(f"Tu promedio es: {prom}")  #mostramos por pantalla el promedio