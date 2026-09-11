#Creamos la lista de golosinas
golosinas = [
    [1,"KitKat",20],
    [2,"Chicles",50],
    [3,"Caramelos de Menta",50],
    [4,"Huevo Kinder",10],
    [5,"Chetoos",10],
    [6,"Twix",10],
    [7,"M&M'S",10],
    [8,"Papas Lays",2],
    [9,"Milkybar",10],
    [10,"Alfajor Tofi",15],
    [11,"Lata Coca",20],
    [12,"chitos",10]
]

#Creamos el diccionario de empleados
empleados = {
    1100:"Jose Alonso",
    1200:"Federico Pacheco",
    1300:"Nelson Pereira",
    1400:"Osvaldo Tejada",
    1500:"Gaston Garcia"    
}
#creamos la clave de tecnico
clavesTecnico = ["admin", "CCCDDD", 2020]
#creamos golosinas pedidas vacia
golosinasPedidas = []

#Funciones Extras/Utiles
def agregarGolosinaPedida(golosina): #Recibe una lista, la golosina como tal. Ejemplo: [2,"KitKat",20]
    """
    Chequea si la golosina se pidio en algun momento. De no ser asi, se ingresa un nuevo array dentro con los valores de la golosina.
    """
    encontrado = False  #inicia encontrado en false
    for i in golosinasPedidas: #Itera sobre todas las golosinas pedidas
        if i[0] == golosina[0]: #si encuentra la golosina entra en el if
            i[2] += 1 #Se le suma uno a las golosina pedida dentro de golosinasPedidas
            encontrado = True # Si la golosina existe dentro de golosinasPedidas, encontrado es True
    if not encontrado: #si encontrado sigue siendo false, se agrega a la lista de golosinas pedidas
        golosinasPedidas.append([golosina[0], golosina[1], 1])


def pedirGolosinas():
    """
    Permite pedir una golosina reduciendo su stock.
    """
    legajoIngresado = int(input("Ingrese su Legajo: "))
    print("\n")
    if legajoIngresado in empleados:
        mostraGolosinas()
        print("\n")
        numeroGolosina = int(input("Ingrese el codigo de la golosina que quiera: "))
        encontrada = False
        for golosina in golosinas:
            if golosina[0] == numeroGolosina:
                encontrada = True
                if golosina[2] > 0:
                    golosina[2] -= 1
                    agregarGolosinaPedida(golosina)
                    print(f"¡Has pedido {golosina[1]} con éxito!")
                    print(f"Stock restante: {golosina[2]}")
                else:
                    print(f"Lo sentimos, la golosina {golosina[1]} no se encuentra disponible.")
                break
        if not encontrada:
            print("El codigo de la golosina es incorrecto")
    else:
        print("Usted no es un empleado de la empresa")


        

def mostraGolosinas():
    """
    Muestra las golosinas disponibles
    """
    for i in golosinas:
        print(i)


def rellenarGolosinas():
    """
    Rellena el stock de las golosinas disponibles. Requiere ingresar con un usuario Correcto
    """
    #Ingreso de 
    usuario = input("Ingrese el Usuario: ")
    ccdd = input("Ingrese los caracteres correctos: ")
    contranumero = int(input("Ingrese el año: "))
    
    #if (usuario, ccdd, contranumero) == clavesTecnico:
    #    print("¡Validación exitosa! Iniciando recarga de golosinas...")

    if usuario == clavesTecnico[0] and ccdd == clavesTecnico[1] and contranumero == clavesTecnico[2]:
        print("¡Validación exitosa! Iniciando recarga de golosinas...")
        while True:
            codigogolosina = int(input("Ingrese el codigo de la golosina que desea rellenar: "))
            if codigogolosina in (1,2,3,4,5,6,7,8,9,10,11,12):
                mostraGolosinas()
                cantidadrecargar = int(input("Ingrese la cantidad que quiera recargar: "))
                if cantidadrecargar > 0:
                    golosinas[codigogolosina-1][2] += cantidadrecargar
                    pregunta = input("Quiere volver a recargar una golosina? S/N: ").upper()
                    if pregunta == 'S':
                        continue
                    else:
                        break
                else:
                    print("La cantidad no puede ser menor a cero")
            else:
                print(f"el codigo {codigogolosina} es incorrecto")
    else:
        print("No tiene permiso para ejecutar la funcion de recarga")

def apagarMaquina():
    for fila in golosinasPedidas: #Itero sobre las golosinas pedidas
        print(fila) # Imprimo las golosinas

    suma = 0 #creamos la suma total
    for golosina in golosinasPedidas: #recorremos todas las golosinas pedidas
        suma += golosina[2] # por cada vez que pase por el stock de cada lista, si es correspondiente se le suma a suma total

    print(f"total de golosinas pedidas: {suma}") #mostramos el total de suma
    print("\t---Apagando Maquina---")


def Menu(): #creacion del menu
    while True:
        print("----------------------\n")
        print("1.Pedir Golosina")
        print("2.Mostrar Golosinas")
        print("3.Rellenar Golosinas")
        print("4.Apagar Maquina")
        eleccion = int(input("Eliga una opcion: ")) #elige la opcion para ingresar al match
        print("----------------------\n")
        
        if eleccion == 1:
            pedirGolosinas()
        elif eleccion == 2:
            mostraGolosinas()
        elif eleccion == 3:
            rellenarGolosinas()
        elif eleccion == 4:
            apagarMaquina()
            break
        else:
            print("Opcion Invalida")
Menu()

