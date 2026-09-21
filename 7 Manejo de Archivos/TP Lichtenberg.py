# ==============================================================================
# PUNTO 1: Crear archivo inicial si no existe (para asegurar la prueba)
# ==============================================================================
with open("productos.txt", "w") as archivo:
    archivo.write("Laptop,1200.0,5\n")
    archivo.write("Mouse,25.5,15\n")
    archivo.write("Teclado,45.0,10\n")


# ==============================================================================
# PUNTO 2 y 4: Leer productos y cargarlos en una lista de diccionarios
# ==============================================================================
productos = []

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        # Limpiamos el salto de línea y separamos por comas
        linea_limpia = linea.strip()
        if linea_limpia:  # Verifica que la línea no esté vacía
            datos = linea_limpia.split(",")
            
            # Guardamos los datos en variables
            nombre = datos[0]
            precio = float(datos[1])
            cantidad = int(datos[2])
            
            # PUNTO 4: Crear el diccionario y agregarlo a la lista
            producto_dic = {
                "nombre": nombre,
                "precio": precio,
                "cantidad": cantidad
            }
            productos.append(producto_dic)

# PUNTO 2: Mostrar productos en el formato requerido
print("--- LISTA DE PRODUCTOS ---")
for p in productos:
    print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")
print("--------------------------\n")


# ==============================================================================
# PUNTO 3: Agregar productos desde teclado
# ==============================================================================
print("--- AGREGAR NUEVO PRODUCTO ---")
nuevo_nombre = input("Ingrese el nombre del nuevo producto: ")
nuevo_precio = float(input("Ingrese el precio: "))
nueva_cantidad = int(input("Ingrese la cantidad: "))

# Lo agregamos a nuestra lista en memoria
nuevo_producto = {
    "nombre": nuevo_nombre,
    "precio": nuevo_precio,
    "cantidad": nueva_cantidad
}
productos.append(nuevo_producto)

# Lo agregamos directamente al archivo en modo append ('a')
with open("productos.txt", "a") as archivo:
    archivo.write(f"{nuevo_nombre},{nuevo_precio},{nueva_cantidad}\n")

print("¡Producto agregado con éxito!\n")


# ==============================================================================
# PUNTO 5: Buscar producto por nombre
# ==============================================================================
print("--- BÚSQUEDA DE PRODUCTO ---")
busqueda = input("Ingrese el nombre del producto a buscar: ")

encontrado = False
for p in productos:
    if p["nombre"].lower() == busqueda.lower():
        print(f"¡Producto encontrado! -> Nombre: {p['nombre']}, Precio: ${p['precio']}, Cantidad: {p['cantidad']}")
        encontrado = True
        break

if not encontrado:
    print(f"Error: El producto '{busqueda}' no se encuentra en el inventario.")
print("---------------------------\n")


# ==============================================================================
# PUNTO 6: Guardar los productos actualizados
# ==============================================================================
# Sobrescribimos el archivo 'productos.txt' con todos los productos de la lista
with open("productos.txt", "w") as archivo:
    for p in productos:
        archivo.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")

print("¡Archivo 'productos.txt' actualizado correctamente con toda la lista!")