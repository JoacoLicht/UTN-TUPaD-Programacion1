
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
                # Pedimos las dos notas
            nota1 = ingresar_nota("Ingrese la Nota 1: ")
            nota2 = ingresar_nota("Ingrese la Nota 2: ")
            materia[1] = nota1 # La nota 1 de la materia
            materia[2] = nota2 # La nota 2 de la materia
            materia[3] = (nota1 + nota2) / 2 # La nota final de la materia
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