from datetime import datetime
from validacion import validacionEntero

def encabezado():
    f=datetime.now()
    dia = f.day
    mes = f.month
    año = f.year
    
    print("\n******************************")
    print("\t¡¡Cabañas!!")
    print("******************************")
    print("     Hoy es:",dia, "-", mes, "-", año)
    print("******************************\n")

def mostrarCabanias():
    f = open('cabins.csv', 'r', encoding="utf-8") #f = open("myfile.txt", "r", encoding="utf-8")
    lineas = f.readlines() # lee todo y guarda en una lista de strings x fila
    # reproduzco todo el archivo de texto en la salida del programa
    lineas.pop(0)
    for li in lineas:
        li = li[:-1].split(',') # le saco el último caracter (salto de línea)
        print(">>> Cabaña nro ",li[0], " habilitada para ",li[1], "personas, tiene un costo de ",li[2], ".\nDisponibilidad: ",li[3], "\nFecha de Ingreso: ",li[4], "\tFecha de Salida: ",li[5])
    print()

def consultarDisponibles():
    f = open('cabins.csv', 'r', encoding="utf-8") #f = open("myfile.txt", "r", encoding="utf-8")
    lineas = f.readlines() # lee todo y guarda en una lista de strings x fila
    # reproduzco todo el archivo de texto en la salida del programa
    lineas.pop(0)
    for li in lineas:
        li = li[:-1].split(',') # le saco el último caracter (salto de línea)
        if li[3] == 'no':
            print(">>> Cabaña nro ", li[0], " habilitada para ", li[1], " personas, tiene un costo de ", li[2])
    print()

def consultarPrecios():
    f = open('cabins.csv', 'r', encoding="utf-8") #f = open("myfile.txt", "r", encoding="utf-8")
    lineas = f.readlines() # lee todo y guarda en una lista de strings x fila
    # reproduzco todo el archivo de texto en la salida del programa
    lineas.pop(0)
    for li in lineas:
        li = li[:-1].split(',') # le saco el último caracter (salto de línea)       
        if li[1] == '4':
            print(">>> Cabaña nro ", li[0]," ", li[2])       
        if li[1] == '3':
            print(">>> Cabaña nro ", li[0]," ", li[2])
        if li[1] == '2':
            print(">>> Cabaña nro ", li[0]," ", li[2])
    print()

def menu():
    encabezado()
    print(">>>Bienvenido<<<\n")
    print("Menú de Opciones\n")
    print("1- Mostrar todas las cabañas con todos sus datos")
    print("2- Consultar disponibles por cantidad de pasajeros")
    print("3- Consultar por rango de precios")
    print("4- Salir\n")
    opcion = validacionEntero(">>> ",min=0,max=4)
    
    if opcion == 1:
        print("\nA continución va a visualizar la información: ")
        mostrarCabanias()
        return menu()
    elif opcion == 2:
        print("\nLas siguientes cabañas son las que se encuentran disponibles: ")
        consultarDisponibles()
        return menu()
    elif opcion == 3:
        print("\nLas cabañas para 4 personas rondan entre $10500 y $12500")
        print("Las cabañas para 3 personas rondan entre $8000 y $11000")
        print("Las cabañas para 2 personas rondan entre $6800 y $8500")
        print("Los valores detallados son los siguientes:\n")
        consultarPrecios()
        return menu()
    elif opcion == 4:
        print("\nExit..\n")
        exit()
    else:
        print("Error.. Ingrese una opcion correcta..")

if __name__ == '__main__':
    menu()
