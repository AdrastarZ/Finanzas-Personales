#Crea una lista con tamaño dependiente de la cantidad de inputs que ponga el usuario hasta que escriba fin
def crea_lista(): 
    lista = []    
    while(True): 
        val = str(input("Añade un sector de gasto (ej. Comida, Renta, Transporte). Escribe 'fin' para terminar: "))
        if val == "fin" or val == "FIN" : #Verifica si el input es fin, y termina de registrar datos para la lista
            break
        elif val.isdigit(): #Verifica si el val entrado no se un numero
            print("No se aceptan datos numéricos. Intente de nuevo")
        else:
            lista.append(val)     
    return lista

#Utiliza la lista creada y solicita valores numericos para añadirlos a una lista con la misma cantidad de posiciones
def futuro_gasto(lista): 
    costo_sector = []
    for i in range(len(lista)):
        costo = int(input(f"Cuanto planea gastar en el sector de {lista[i]}: "))
        costo_sector.append(costo)
    return costo_sector

#Utilizando la lista de sectores y la lista numerica, las combina y las transforma un mensaje en orden de sus posiciones
def sector_costo(lista, costo):
    mensajes = []
    for i in range(len(lista)):
        mensaje = f"En el sector {lista[i]} tienes planeado gastar ${costo[i]} pesos"
        mensajes.append(mensaje)
    return mensajes

#Utilizando la lista numerica, suma todos los valores de todas las posiciones y lo divide junto con los valores individuales para sacar porcentaje
def porcentajes(lista, costo):
    percent = 0
    suma = 0
    mensajes = []
    for s in range(len(costo)):
        suma += costo[s]

    for i in range(len(costo)):
        percent = (costo[i]/suma)*100
        mensaje = f"En el sector {lista[i]} tienes un presupuesto planeado del {percent:.2f}% del total"
        mensajes.append(mensaje)
    return mensajes

#Utilizando la lista numerica y sumando todos los valores de cada posicion, 
# y preguntando las ganancias mensuales se saca una diferencia para verificar si sobra dinero o no
def sobrante(ganancias, costo):
    mensaje = ""
    suma = 0
    for s in range(len(costo)):
        suma += costo[s]
    res = ganancias - suma
    if ganancias > suma:
        mensaje = f"Acorde a tu presupuesto, tienes ${res} sobrante"
    elif ganancias == suma:
        mensaje = f"Acorde a tu presupuesto, tienes la cantidad justa de dinero ${res}"
    elif ganancias < suma:
        mensaje = f"Acorde a tu presupuesto, tus ganancias no cubren todo tu presupuesto mensual ${res}"
    
    return mensaje

#Casos de prueba para todas las funciones
def casos_prueba():
    ganancias = 1000
    sectores = ["Comida", "Salud", "Infraestructura", "Educativo", "Ahorros"]
    costo = [250, 125, 50, 400, 150]

    print("INICIANDO CASOS DE PRUEBA \n")

    print("Función de sector_costo")
    for m in sector_costo(sectores, costo):
        print(m,"\n")

    print("Función de porcentajes")
    for m in porcentajes(sectores, costo):
        print(m ,"\n")

    print("Función de dinero sobrante")
    print(sobrante(ganancias,costo) ,"\n")

def menu():
    print("\n 1. Costo por sector \n 2. Porcentaje de costo por sector \n " 
    "3. Dinero sobrante \n 4. Casos de prueba \n 5. Salir")

def main():
    while(True):
        menu()
        opcion = int(input("Selecciona una opcion del menu: "))
        if(opcion == 1):
            lista = crea_lista()
            costo = futuro_gasto(lista)
            for m in sector_costo(lista, costo): #Para que cada lista salga ordenada se aplica un for para cada funcion
                print(m)

        elif(opcion == 2):
            lista = crea_lista()
            costo = futuro_gasto(lista)
            for m in porcentajes(lista, costo):#Para que cada lista salga ordenada se aplica un for para cada funcion
                print(m)

        elif(opcion == 3):
            lista = crea_lista()
            costo = futuro_gasto(lista)
            ganancias = int(input("¿Cuanto ganas mensualmente? "))
            print(sobrante(ganancias,costo))

        elif(opcion == 4):
            casos_prueba()
        elif(opcion == 5):
            print("Saliendo de la sesión")
            break
        else:
            print("Opción no valida, saliendo de la sesión")
            break

main()



