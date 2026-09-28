# ==============================================================================
# GUÍA DE REPASO DE PYTHON: ESTRUCTURAS, OPERACIONES, CLASES Y RECURSIVIDAD
# ==============================================================================

# ==============================================================================
# 1. GUÍA COMPLETA DE COLECCIONES DE DATOS
# ==============================================================================

# ------------------------------------------------------------------------------
# A) LISTAS (Ordenadas, mutables, permiten duplicados)
# ------------------------------------------------------------------------------
print("--- A) LISTAS ---")
lista = ["manzana", "banana", "cereza"]

# LLAMAR / ACCEDER
print("Acceder por índice (0):", lista[0])           # Primer elemento
print("Acceder al último:", lista[-1])               # Último elemento
print("Slicing (recorte 0 a 2):", lista[0:2])        # Sublista sin incluir el índice 2

# AGREGAR
lista.append("naranja")            # Agrega al final
lista.insert(1, "uva")             # Inserta en un índice específico
lista.extend(["pera", "kiwi"])     # Agrega múltiples elementos de otra lista
print("Lista tras agregar:", lista)

# MODIFICAR
lista[0] = "manzana roja"          # Modificación directa por índice

# ELIMINAR
lista.remove("banana")             # Elimina por VALOR (primera ocurrencia)
eliminado = lista.pop(2)           # Elimina por ÍNDICE y lo retorna (default: último)
del lista[0]                       # Elimina elemento en índice o rango
print(f"Lista tras eliminar (se extrajo '{eliminado}'):", lista)

# MOVER / REORDENAR / ORGANIZAR
numeros = [5, 2, 9, 1, 7]
numeros.sort()                     # Ordena la lista original en orden ascendente
print("Orden ascendente:", numeros)
numeros.sort(reverse=True)         # Ordena en orden descendente
print("Orden descendente:", numeros)
numeros.reverse()                  # Invierte el orden actual de los elementos
print("Lista invertida:", numeros)


# ------------------------------------------------------------------------------
# B) TUPLAS (Ordenadas, INMUTABLES, permiten duplicados)
# ------------------------------------------------------------------------------
print("\n--- B) TUPLAS ---")
tupla = ("rojo", "verde", "azul", "rojo")

# LLAMAR / ACCEDER
print("Acceder por índice (1):", tupla[1])
print("Contar ocurrencias de 'rojo':", tupla.count("rojo"))
print("Buscar índice del valor 'verde':", tupla.index("verde"))

# AGREGAR / ELIMINAR / MODIFICAR:
# Las tuplas NO permiten agregar, eliminar ni modificar directamente.
# TRUCO EVALUACIÓN: Convertir a lista -> modificar -> reconvertir a tupla
temp_lista = list(tupla)
temp_lista.append("amarillo")
temp_lista.remove("rojo")
tupla_modificada = tuple(temp_lista)
print("Tupla modificada indirectamente:", tupla_modificada)


# ------------------------------------------------------------------------------
# C) DICCIONARIOS (Pares Clave: Valor, mutables, claves únicas)
# ------------------------------------------------------------------------------
print("\n--- C) DICCIONARIOS ---")
estudiante = {"nombre": "Carlos", "edad": 20, "materia": "Programación"}

# LLAMAR / ACCEDER
print("Acceder por clave:", estudiante["nombre"])
print("Acceder de forma segura con .get():", estudiante.get("promedio", "No registrado"))
print("Obtener todas las claves:", list(estudiante.keys()))
print("Obtener todos los valores:", list(estudiante.values()))
print("Obtener pares (clave, valor):", list(estudiante.items()))

# AGREGAR Y MODIFICAR
estudiante["promedio"] = 8.5        # Agrega si la clave no existe
estudiante["edad"] = 21             # Modifica si la clave ya existe
estudiante.update({"legajo": 1234, "materia": "Algoritmos"})  # Agrega/Actualiza en lote
print("Diccionario actualizado:", estudiante)

# ELIMINAR
valor_borrado = estudiante.pop("edad")   # Elimina clave y retorna su valor
del estudiante["materia"]                # Elimina por clave directa
print(f"Tras borrar 'edad' ({valor_borrado}) y 'materia':", estudiante)

# MOVER / REORGANIZAR
# Convertir a lista de tuplas ordenadas por clave:
dicc_ordenado = dict(sorted(estudiante.items()))
print("Diccionario ordenado por sus claves:", dicc_ordenado)


# ------------------------------------------------------------------------------
# D) SETS / CONJUNTOS (Desordenados, mutables, NO permiten elementos duplicados)
# ------------------------------------------------------------------------------
print("\n--- D) SETS (CONJUNTOS) ---")
conjunto = {"python", "java", "c++"}

# LLAMAR / VERIFICAR
# Los sets NO tienen índices. Se accede iterando o verificando presencia:
print("¿Está 'python' en el set?:", "python" in conjunto)

# AGREGAR
conjunto.add("javascript")          # Agrega un elemento
conjunto.update(["html", "css"])     # Agrega múltiples elementos de una lista/set
print("Set tras agregar elementos:", conjunto)

# ELIMINAR
conjunto.remove("java")              # Elimina elemento (Lanza ERROR si no existe)
conjunto.discard("php")              # Elimina elemento (NO lanza error si no existe)
eliminado_set = conjunto.pop()       # Elimina y retorna un elemento ALEATORIO
print(f"Set tras eliminar (pop quitó '{eliminado_set}'):", conjunto)

# OPERACIONES DE CONJUNTOS (Muy evaluadas)
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print("Unión (A | B):", set_a.union(set_b))             # {1, 2, 3, 4, 5, 6}
print("Intersección (A & B):", set_a.intersection(set_b)) # {3, 4}
print("Diferencia (A - B):", set_a.difference(set_b))     # {1, 2}


# ==============================================================================
# 2. RECURSIVIDAD
# Una función que se llama a sí misma para resolver subproblemas más pequeños.
# REGLA DE ORO: Siempre debe tener un "Caso Base" para cortar la ejecución.
# ==============================================================================
print("\n--- 2. RECURSIVIDAD ---")

def factorial(n):
    """
    Calcula el factorial de n (n!).
    Ejemplo: 5! = 5 * 4 * 3 * 2 * 1 = 120
    """
    # 1. CASO BASE: Detiene las llamadas recursivas
    if n == 0 or n == 1:
        return 1
    
    # 2. CASO RECURSIVO: La función se llama a sí misma con un problema reducido
    else:
        return n * factorial(n - 1)

print("Factorial de 5:", factorial(5))


def suma_recursiva_lista(lista):
    """Suma los elementos de una lista usando recursividad."""
    if not lista:  # Caso base: lista vacía
        return 0
    else:          # Caso recursivo: primer elemento + suma del resto de la lista
        return lista[0] + suma_recursiva_lista(lista[1:])

print("Suma recursiva de [2, 4, 6]:", suma_recursiva_lista([2, 4, 6]))


# ==============================================================================
# 3. CLASES Y PROGRAMACIÓN ORIENTADA A OBJETOS (POO)
# Una clase es una plantilla para crear objetos con atributos y métodos.
# ==============================================================================
print("\n--- 3. CLASES Y POO ---")

class Persona:
    """Definición de la clase Persona."""

    # Método constructor: Se ejecuta automáticamente al instanciar el objeto
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo de instancia
        self.edad = edad      # Atributo de instancia

    # Método de instancia: Comportamiento que la persona puede realizar
    def saludar(self):
        return f"Hola, me llamo {self.nombre} y tengo {self.edad} años."

    def cumplir_anios(self):
        self.edad += 1
        return f"¡Feliz cumpleaños {self.nombre}! Ahora tienes {self.edad} años."


# Instanciación de objetos (Creación de instancias)
persona1 = Persona("Ana", 20)
persona2 = Persona("Lucas", 22)

# Llamada a métodos y acceso a atributos
print(persona1.saludar())
print(persona1.cumplir_anios())
print(f"Atributo directo de persona2: {persona2.nombre}")


# CONCEPTO DE HERENCIA (Extender el comportamiento de una clase)
class Estudiante(Persona):
    """Clase Hija que hereda de Persona."""

    def __init__(self, nombre, edad, carrera):
        # Llama al constructor de la clase padre (Persona)
        super().__init__(nombre, edad)
        self.carrera = carrera  # Nuevo atributo propio del estudiante

    def estudiar(self):
        return f"{self.nombre} está estudiando la carrera de {self.carrera}."


# Crear instancia de la clase derivada
estudiante1 = Estudiante("Sofía", 19, "Ingeniería en Sistemas")
print(estudiante1.saludar())   # Método heredado de Persona
print(estudiante1.estudiar())  # Método propio de Estudiante