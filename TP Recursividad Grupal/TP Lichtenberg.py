class Archivo:
    def __init__(self, nombre: str, tamano_bytes: int):
        self.nombre = nombre
        self.tamano_bytes = tamano_bytes

class Directorio:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.archivos = []         # Lista de objetos de tipo Archivo
        self.subdirectorios = []    # Lista de objetos de tipo Directorio


# ==========================================
# 1. CÁLCULO DEL TAMAÑO TOTAL
# ==========================================
def calcular_tamano_total(directorio: Directorio) -> int:
    """
    Suma el tamaño de todos los archivos del directorio actual 
    y llama recursivamente para sumar el tamaño de sus subdirectorios.
    """
    # Suma local de los archivos del directorio actual
    total_local = sum(archivo.tamano_bytes for archivo in directorio.archivos)
    
    # Caso Base (implícito): Si subdirectorios está vacío, no entra al loop 
    # y retorna solo total_local.
    # Paso Recursivo: Sumar el resultado de cada subdirectorio.
    total_subdirectorios = sum(calcular_tamano_total(sub) for sub in directorio.subdirectorios)
    
    return total_local + total_subdirectorios


# ==========================================
# 2. BÚSQUEDA DE ARCHIVOS POR EXTENSIÓN
# ==========================================
def buscar_por_extension(directorio: Directorio, extension: str, ruta_actual: str = "") -> list[str]:
    """
    Busca archivos que terminen con una extensión específica en toda la jerarquía 
    y retorna una lista con sus rutas completas.
    """
    if not ruta_actual:
        ruta_actual = directorio.nombre
    else:
        ruta_actual = f"{ruta_actual}/{directorio.nombre}"

    coincidencias = []

    # Revisa archivos locales
    for archivo in directorio.archivos:
        if archivo.nombre.endswith(extension):
            coincidencias.append(f"{ruta_actual}/{archivo.nombre}")

    # Llamada recursiva a los subdirectorios
    for sub in directorio.subdirectorios:
        coincidencias.extend(buscar_por_extension(sub, extension, ruta_actual))

    return coincidencias


# ==========================================
# 3. ELIMINACIÓN RECURSIVA DE ARCHIVOS VACÍOS
# ==========================================
def limpiar_archivos_vacios(directorio: Directorio) -> int:
    """
    Elimina los archivos con tamaño 0 bytes y retorna la cantidad 
    total de archivos eliminados en la jerarquía.
    """
    archivos_iniciales = len(directorio.archivos)
    
    # Conservar solo aquellos archivos con tamaño mayor a 0
    directorio.archivos = [a for a in directorio.archivos if a.tamano_bytes > 0]
    
    eliminados_locales = archivos_iniciales - len(directorio.archivos)

    # Paso Recursivo: Limpiar en cada subdirectorio y acumular
    eliminados_subdirectorios = sum(limpiar_archivos_vacios(sub) for sub in directorio.subdirectorios)

    return eliminados_locales + eliminados_subdirectorios


# ==========================================
# 4. CASO DE PRUEBA Y VALIDACIÓN
# ==========================================
if __name__ == "__main__":
    # Construcción de la estructura
    root = Directorio("root")
    
    # Archivos locales en root/
    root.archivos.append(Archivo("documento.pdf", 1500))
    root.archivos.append(Archivo("config.txt", 0))

    # Subdirectorio imagenes/
    imagenes = Directorio("imagenes")
    imagenes.archivos.append(Archivo("foto1.png", 2000))
    imagenes.archivos.append(Archivo("foto2.png", 3500))
    root.subdirectorios.append(imagenes)

    # Subdirectorio proyectos/
    proyectos = Directorio("proyectos")
    proyectos.archivos.append(Archivo("avance.pdf", 800))
    
    # Subdirectorio temp/ dentro de proyectos/
    temp = Directorio("temp")
    temp.archivos.append(Archivo("log.txt", 0))
    proyectos.subdirectorios.append(temp)
    
    root.subdirectorios.append(proyectos)

    # --- EJECUCIÓN Y VALIDACIÓN ---
    print("--- PRUEBAS DE VALIDACIÓN ---")
    
    # Prueba 1: Tamaño total
    tamano_total = calcular_tamano_total(root)
    print(f"1. Tamaño Total: {tamano_total} bytes")
    
    # Prueba 2: Búsqueda por extensión
    archivos_pdf = buscar_por_extension(root, ".pdf")
    print(f"2. Archivos PDF encontrados: {archivos_pdf}")
    print(f"   Esperado: ['root/documento.pdf', 'root/proyectos/avance.pdf']")

    # Prueba 3: Limpieza de archivos vacíos
    eliminados = limpiar_archivos_vacios(root)
    print(f"3. Archivos vacíos eliminados: {eliminados}")

    # Comprobación adicional post-limpieza
    tamano_post_limpieza = calcular_tamano_total(root)
    print(f"   Tamaño total tras la limpieza: {tamano_post_limpieza} bytes")