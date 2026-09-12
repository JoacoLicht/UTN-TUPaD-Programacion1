import os # importamos libreria de sistema operativo

alumnos= { #creamos un diccionario de alumnos con su legajo
    60902: "Rodolfo Fernandez",
    61654: "Luis Gomez",
    61852: "Andrea Pereira",
    61754: "Juan Cruz Gonzales"
}

materias = [ #creamos una lista que contiene listas de materias y sus notas iniciadas en 0
    ["Ciencias",0,0,0],
    ["Historia",0,0,0],
    ["Geografia",0,0,0],
    ["Matematicas",0,0,0],
    ["Fisica",0,0,0]
]  

notasFinales = [ #creamos una lista de notas finales con los nombres de los estudiantes
    ["Rodolfo Fernandez",0],
    ["Luis Gomez",0],
    ["Andrea Pereira",0],
    ["Juan Cruz Fernandez",0]
]

def pedirNotas(): #creamos una funcion para pedir las notas de cada alumno
    """
    Itera sobre las materias de cada alumno, pidiendo nota 1 y 2 de cada materia.
    """
    contador = 0 #iniciamos el contador en 0
    for alumno in alumnos: #Iteramos sobre los alumnos
        print("\n\n------------------------------")
        print(f"\t Alumno: {alumnos[alumno]}")
        for materia in materias: #Iteramos sobre las materias
            print(f"\t Materia: {materia[0]}")
            while True:
                # Pedimos las dos notas
                nota1 = int(input("Ingrese la Nota 1: "))
                nota2 = int(input("Ingrese la Nota 2: "))
                if 0 <= nota1 <= 10 and 0 <= nota2 <= 10: #Chequeamos que esten entre 0 y 10
                    break
                else:
                    print("Error: Las notas deben estar entre 0 y 10. Intente de nuevo.")
            materia[1] = nota1 # La nota 1 de la materia
            materia[2] = nota2 # La nota 2 de la materia
            materia[3] = (nota1 + nota2) / 2 # La nota final de la materia
            limpiarPantalla() # Limpiamos la pantalla
        print("\n\n------------------------------")
        print(f"- Alumno: {alumnos[alumno]}")
        mostrarMaterias()
        notasFinales[contador][1] = notaFinal()
        contador += 1

def mostrarMaterias():
    """
    Mostramos todas las materias con sus notas, la materia con calificacion mas alta y el promedio
    """
    print("\t---Materias---")
    for materia in materias:
        print(materia)
    print(f"Materia con la calificacion mas alta: {materiaCalificacionAlta()}")
    print(f"Promedio General {notaFinal()}")

def materiaCalificacionAlta():
    """
    Retorna la materia que contenga la calificacion mas alta
    """
    notaMateriaMasAlta = 0
    nombreMateriaMasAlta = ""
    for materia in materias:
        if materia[3] > notaMateriaMasAlta:
            notaMateriaMasAlta = materia[3]
            nombreMateriaMasAlta = materia[0] 
    return nombreMateriaMasAlta

def notaFinal():
    """
    Returna: La nota final
    """
    notaFinal = 0
    for materia in materias:
        notaFinal += materia[3]
    return notaFinal / len(materias)

def limpiarPantalla():

    """
    Limpia la pantalla
    """
    os.system('cls')#ejecuta un comando en la terminal, que en este caso utiliza cls(limpiar la pantalla)

def alumnoPromedioMasAlto():
    notaMasAlta = 0
    nombreAlumno = ""
    for notas in notasFinales:
        if notas[1] > notaMasAlta:
            notaMasAlta = notas[1]
            nombreAlumno = notas[0]
    print("\t---ALUMNO CON LA NOTA MAS ALTA---")
    print(f"Nombre: {nombreAlumno}")
    print(f"Su Nota: {notaMasAlta}")

def Menu():
    pedirNotas()
    alumnoPromedioMasAlto()

Menu()