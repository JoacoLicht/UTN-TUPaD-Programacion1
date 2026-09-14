print("\t----------EJERCICIO 1----------\n") 
def imprimir_hola_mundo(): #creamos la funcion def
    print("Hola mundo!")

imprimir_hola_mundo() #llamamos a la funcion

print("\t----------EJERCICIO 2----------\n")

def saludar_usuario(nombre): #creamos la funcion con parametro nombre
    return f"Hola {nombre}!"

nombreIngresado = input("Escriba su nombre: ") 
saludo = saludar_usuario(nombreIngresado) #guardamos la funcion con el nombre ingresado en un "saludo" para poder mostrarlo por pantalla
print(saludo) #mostramos el saludo

print("\t----------EJERCICIO 3----------\n")

def informacion_Personal(nombre,apellido,edad,residencia): #creamos la funcion con 4 parametros
    return f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}" #retornamos el resultado

#pedimos la informacion deseada
nombreinfo = input("Nombre: ")
apellidoinfo = input("Apellido: ") 
edadinfo = int(input("Edad: "))
residenciainfo = input("Lugar de residencia: ")

info = informacion_Personal(nombreinfo,apellidoinfo,edadinfo,residenciainfo) #llamamos a la funcion guardando su resultado en una variable llamada "info"
print(info)#mostramos el resultado

print("\t----------EJERCICIO 4----------\n")

#importamos PI de matematicas
from math import pi

#creamos la funcion del area de un circulo con 1 parametro
def calcular_area_circulo(radio):
 area = pi * radio**2 #calculamos el area
 return area #retornamos area

#creamos la funcion perimetro de un circulo
def calcular_perimetro_circulo(radio):
    perimetro = 2* pi * radio #calculamos el perimetro
    return perimetro #retornamos el perimetro

radio = int(input("Ingrese el radio: ")) #pedimos que ingrese el radio

arearadio = calcular_area_circulo(radio) #llamamos a la funcion de area y la guardamos en una variable de arearadio, enviandole el radio
perimetroradio = calcular_perimetro_circulo(radio)#llamamos a la funcion de perimetro y la guardamos en una variable de perimetroradio, enviandole el radio

print(f"El area de un circulo es: {arearadio} y el perimetro es: {perimetroradio}") #mostramos el resultado por pantalla

print("\t----------EJERCICIO 5----------\n")

#creamos una funcion con 1 parametro
def segundos_a_horas(segundos):
   horastotal = segundos / 3600 #calculamos los segundos y los convertimos en horas
   return horastotal #retornamos las horas

usuariosegundos = int(input("Ingrese los segundo: ")) #pedimos que ingrese los segundos
horas= segundos_a_horas(usuariosegundos) #llamamos a la funcion y la guardamos en una variable llamada horas, enviandole los segundos pedidos
print(f"El total de {usuariosegundos} segundos, equivale a {horas} horas") #mostramos el resultado por pantalla

print("\t----------EJERCICIO 6----------\n")

#creamos la funcion con 1 parametro
def tabla_multiplicar(numero):
  
    # for i in range(1, 11):
    #      resultado = numero * i
    #     print(f"{numero} x {i} = {resultado}"

   #retornamos el resultado
  return (f""" 
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
      """) 

numeromultiplicar = int(input("Ingrese el numero a multiplicar: "))#pedimos al usuario el numero a multiplicar
multiplicado = tabla_multiplicar(numeromultiplicar)#llamamos a la funcion y la guardamos en una variable
print(multiplicado)#mostramos por pantalla

print("\t----------EJERCICIO 7----------\n")

#creamos la funcion con 2 parametros
def operaciones_basicas(a,b):
    suma =a+b
    resta =a-b
    multi =a*b
#hacemos un if para ver que no divida por 0
    if b != 0:
       divi = a/b
    else:
       divi = "No se puede dividir por 0"
    return (suma, resta, multi, divi) #retornamos los 4 valores

numero1 = int(input("Ingrese el primer numero: ")) #ingresamos numero 1
numero2 = int(input("Ingrese el segundo numero: "))#ingresamos numero 2

s, r, m, d= operaciones_basicas(numero1,numero2) #asigna directamente cada valor dentro de la tupla devuelta a una variable individual distinta en el programa principal.

#mostramos los resultados
print("\n--- Resultados ---")
print(f"Suma ({numero1} + {numero2}): {s}")
print(f"Resta ({numero1} - {numero2}): {r}")
print(f"Multiplicación ({numero1} * {numero2}): {m}")
print(f"División ({numero1} / {numero2}): {d}")

print("\t----------EJERCICIO 8----------\n")

#creamos la funcion con 2 parametros
def calcular_imc(peso,altura):
   imc = peso / (altura**2) #calculamos la masa
   return imc #retornamos el resultado
   
#pedimos al usuario los datos
pesoinfo = float(input("Ingrese su peso en kilogramos: "))
alturainfo = float(input("Ingrese su altura en metros: "))

indiceMasa = calcular_imc(pesoinfo,alturainfo) #llamamos a la funcion y la guardamos en una variable
print(f"Su indice de masa corporal es: {indiceMasa:.2f}")#mostramos por pantalla con dos decimales

print("\t----------EJERCICIO 9----------\n")

#creamos la funcion con 1 parametro
def celsius_a_fahrenheit(celsius):
   return (celsius*9/5)+32 #retornamos el resultado

celsiusinfo = int(input("Ingrese los grados en Celsius: "))#pedimos al usuario los celsius
celsiusResultado = celsius_a_fahrenheit(celsiusinfo)#llamamos a la funcion y la guardamos en una variable
print(f"Los grados {celsiusinfo} en Celsius equivalen a {celsiusResultado} en Fahrenheit")#mostramos por pantalla el resultado

print("\t----------EJERCICIO 9----------\n")

#creamos la funcion con 3 parametros
def calcular_promedio(a,b,c):
   return (a+b+c)/3 #retornamos el resultado

#pedimos al usuario los 3 numeros
promedio1 = int(input("Ingrese la nota 1: "))
promedio2 = int(input("Ingrese la nota 2: "))
promedio3 = int(input("Ingrese la nota 3: "))

resultadoPromedio = calcular_promedio(promedio1,promedio2,promedio3)#llamamos a la funcion y la guardamos en una variable
print(f"El promedio de las notas es: {resultadoPromedio:.2f}")#mostramos el resultado por pantalla