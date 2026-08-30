#Ejercicio 1
print("\t----------EJERCICIO 1----------\n")

multiplos = list(range(4,101,4)) #creamos una lista que contenga un rango del 4 al 100, con paso de 4
print(multiplos)

#Ejercicio 2
print("\t----------EJERCICIO 2----------\n")

elementos5 =["Azul","Morado","Rojo","Amarillo","Celeste"] #Creamos una lista con 5 elementos

print(elementos5[3]) # mostramos el elemento seleccionando el indice 3 de la lista
print(elementos5[-2]) # podemos mostrarlo con -2, que lo que hace es ir de atras hacia adelante

#Ejercicio 3
print("\t----------EJERCICIO 3----------\n")

lista_vacia=[] #creamos una lista vacia

lista_vacia.append("Foco")
lista_vacia.append("Mesa")  #agregamos 3 palabras a la lista
lista_vacia.append("Silla")

print(lista_vacia) #mostramos por pantalla

#Ejercicio 4
print("\t----------EJERCICIO 4----------\n")

animales = ["perro","gato","conejo","pez"] #creamos la lista

animales[1] = "loro" #cambiamos la palabra indicando el indice
animales[-1] = "oso" # cambiamos con numero/indice negativo, para obtener el ultimo de la lista
print(animales)

#Ejercicio 5
print("\t----------EJERCICIO 5----------\n")

print("Crea una lista con 5 valores, luego calcula el maximo y lo elimina, despues muestra la lista sin el numero mas grande")

#Ejercicio 6
print("\t----------EJERCICIO 6----------\n") 

hastael30= list(range(10,31,5)) #creamos una lista con rango del 10 al 31 con salto de 5
print(hastael30[0]) #Obtengo el primer numero
print(hastael30[1]) #Obtengo el segundo numero

#Ejercicio 7
print("\t----------EJERCICIO 7----------\n") 

autos =["sedan","polo","suran","gol"] #creamos la lista autos con 4 valores
autos[1] = "Ferrari"
autos[2]= "Bugatti" #cambiamos los dos valores centrales por otros valores
print(autos)

#Ejercicio 8
print("\t----------EJERCICIO 8----------\n") 

dobles = [] #creamos una lista vacia
dobles.append(5*2)
dobles.append(10*2) #agregamos 3 valores multiplicados por 2
dobles.append(15*2)
print(dobles) #mostramos por pantalla

#Ejercicio 9
print("\t----------EJERCICIO 9----------\n") 

compras = [["pan","leche"], ["arroz","fideos","salsa"], ["agua"]]

#a) Agregar "jugo" a la lista del tercer cliente usando append
compras[2].append("jugo")
#b) Remplazar "fideos" por "tallarines" en la lista del segundo cliente
compras[1][1]= "tallarines"
#c) Eliminar "pan" de la lista del primer cliente
compras[0].remove("pan")
#d) Imprimir al lista resultante
print(compras)

#Ejercicio 10
print("\t----------EJERCICIO 10----------\n") 

lista_anidada= [15, True, [25.5, 57.9, 30.6],False] #creamos una lista anidada
print(lista_anidada)