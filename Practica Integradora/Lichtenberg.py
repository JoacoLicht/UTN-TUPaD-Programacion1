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
clavesTecnico = ("admin", "CCCDDD",2020)
#creamos golosinas pedidas vacia
golosinasPedidas = [
    [10,"Alfajor Tofi",1],
    [11,"Lata Coca",2],
    [12,"chitos",1],
]

#Funciones Extras/Utiles
def agregarGolosinaPedida(golosina: []): #Recibe una lista, la golosina como tal. Ejemplo: [2,"KitKat",20]
    """
    Chequea si la golosina se pidio en algun momento. De no ser asi, se ingresa un nuevo array dentro con los valores de la golosina
    """
    for i in golosinasPedidas: #Itera sobre todas las golosinas pedidas
        encontrado = False  #inicia encontrado en false
        if i[0] == golosina[0]: #si encuentra la golosina entra en el if
            i[2] += 1 #Se le suma uno a las golosina pedida dentro de golosinasPedidas
            encontrado = True # Si la golosina existe dentro de golosinasPedidas, encontrado es True
    if not encontrado: #si encontrado sigue siendo false, se agrega a la lista de golosinas pedidas
        golosinasPedidas.append(golosina)



def pedirGolosinas():
    legajoIngresado = int(input("Ingrese su Legajo: "))
    if legajoIngresado in empleados.keys():
        mostraGolosinas()
        numeroGolosina = int(input("Ingrese el codigo de la golosina que quiera: "))
        for golosina in golosinas: #Iteramos sobre todas las golosinas
            if golosina[0] == numeroGolosina: #Chequeamos si la golosina existe, comparando su codigo con el ingresado
                if golosina[2] > 0: #Chequeamos si hay stock
                    golosina[2] -= 1 #restamos stock
                    agregarGolosinaPedida(golosina=[]) #Funcion para ingresar
                else:
                    print(f"Lo sentimos la golosina {golosina[1]} no se encuentra disponible o no hay stock.")
            else: 
                print("Esa golosina no existe.")
    else:
        print("Usted no es un empleado de la empresa")
        

def mostraGolosinas():
    pass

def rellenarGolosinas():
    pass

def apagarMaquina():
    pass


opcion = True
while opcion:
    #Codigo de referencia hasta que el valor de la opcion sea igual a false, y el programa termina
    pass