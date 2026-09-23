# 1. Creamos el archivo inicial de prueba con formato ";" (separado por punto y coma)
with open("alumnos.txt", "w") as archivo:
    archivo.write("Juan;Pérez;53365;8\n")
    archivo.write("María;López;55654;10\n")
    archivo.write("Pablo;Gómez;58999;6\n")


def leer_alumnos():
    alumnos_lista = []
    diccionario_alumnos = {}

    with open("alumnos.txt", "r") as archivo:
        for linea in archivo:
            linea_limpia = linea.strip()
            if linea_limpia != "":
                # Separamos los datos usando punto y coma ";"
                nombre, apellido, legajo, notaPromedio = linea_limpia.split(";")
                
                # Guardamos en la lista
                alumnos_lista.append({
                    "nombre": nombre,
                    "apellido": apellido,
                    "legajo": legajo,
                    "nota": notaPromedio
                })
                
              # Guardamos en el diccionario con el legajo como clave
                diccionario_alumnos[legajo] = {
                    "nombre": nombre,
                    "apellido": apellido,
                    "nota": notaPromedio
                }

    return alumnos_lista, diccionario_alumnos


def validar_existe_alumno(legajo, diccionario_alumnos):
    # Verificamos si la clave 'legajo' existe en el diccionario
    if legajo in diccionario_alumnos:
        print(f"El legajo {legajo} ya existe en el archivo alumnos.txt, no se permite su escritura")
        return True
    return False


def agregar_alumno(diccionario_alumnos):
    print("\n--- AGREGAR NUEVO ALUMNO ---")

    # 1. Validar Nombre (solo letras)
    while True:
        nombre = input("Ingrese Nombre: ").strip()
        if nombre.isalpha():
            break
        print("El nombre solo debe contener letras.")

    # 2. Validar Apellido (solo letras)
    while True:
        apellido = input("Ingrese Apellido: ").strip()
        if apellido.isalpha():
            break
        print("El apellido solo debe contener letras.")

    # 3. Validar Legajo (5 dígitos)
    while True:
        legajo = input("Ingrese Legajo (5 dígitos): ").strip()
        if legajo.isdigit() and len(legajo) == 5:
            break
        print("El legajo debe ser un número entero de exactamente 5 dígitos.")

    # 4. Validar si ya existe el legajo
    if validar_existe_alumno(legajo, diccionario_alumnos):
        return  # Si ya existe, salimos de la función y cancelamos la carga

   # 5. Validar Nota Promedio (número entre 1 y 10)
    while True:
        nota_str = input("Ingrese Nota Promedio (1-10): ").strip()
        
        # Guardamos en un texto todos los caracteres válidos para un número
        caracteres_validos = "0123456789."
        
        # Verificamos si la cadena no está vacía y si todos sus caracteres son válidos
        es_valido = True
        puntos = 0
        
        if nota_str == "":
            es_valido = False
        else:
            for caracter in nota_str:
                # Comprobamos si el caracter está en nuestra lista de caracteres permitidos
                if caracter not in caracteres_validos:
                    es_valido = False
                    break
                # Contamos cuántos puntos tiene para no aceptar cosas como "8..5" o "8.5.2"
                if caracter == ".":
                    puntos = puntos + 1

        # Si tiene más de un punto, tampoco es válido
        if puntos > 1:
            es_valido = False

        if es_valido:
            nota_num = float(nota_str)
            if 1 <= nota_num <= 10:
                notaPromedio = nota_str
                break
            else:
                print("La nota debe estar entre 1 y 10.")
        else:
            print("Debe ingresar un valor numérico para la nota.")

    # 6. Escribir el nuevo alumno al final de alumnos.txt (Modo 'a')
    with open("alumnos.txt", "a") as archivo:
        archivo.write(f"{nombre};{apellido};{legajo};{notaPromedio}\n")

    print("¡Alumno agregado exitosamente!")


def guardar_aprobados():
    alumnos_lista, _ = leer_alumnos()

    # 1. Guardar solo a los aprobados (nota >= 6) en aprobados.txt
    with open("aprobados.txt", "w") as archivo_aprobados:
        for alumno in alumnos_lista:
            if float(alumno["nota"]) >= 6:
                linea = f"{alumno['nombre']};{alumno['apellido']};{alumno['legajo']};{alumno['nota']}\n"
                archivo_aprobados.write(linea)

    print("\n--- CONTENIDO DE APROBADOS.TXT ---")
    
    # 2. Leer y mostrar por pantalla el archivo generado
    with open("aprobados.txt", "r") as archivo_aprobados:
        contenido = archivo_aprobados.read()
        if contenido.strip() != "":
            print(contenido)
        else:
            print("No hay alumnos aprobados.")


# --- BUCLE PRINCIPAL DEL PROGRAMA ---
while True:
    # Leemos al inicio de cada iteración para tener los datos del diccionario al día
    alumnos_lista, diccionario_alumnos = leer_alumnos()

    print("\n========== MENÚ DE OPCIONES ==========")
    print("1. Ver alumnos")
    print("2. Agregar alumno")
    print("3. Generar y mostrar archivo de aprobados")
    print("4. Salir")
    print("=======================================")
    
    opcion = input("Ingrese una opción (1-4): ").strip()

    if opcion == "1":
        print("\n--- LISTA DE ALUMNOS ---")
        for alumno in alumnos_lista:
            print(f"Nombre: {alumno['nombre']} | Apellido: {alumno['apellido']} | Legajo: {alumno['legajo']} | Nota: {alumno['nota']}")
            
    elif opcion == "2":
        agregar_alumno(diccionario_alumnos)
        
    elif opcion == "3":
        guardar_aprobados()
        
    elif opcion == "4":
        print("-- Saliendo del programa --")
        break
        
    else:
        print("Opción inválida. Intente nuevamente.")