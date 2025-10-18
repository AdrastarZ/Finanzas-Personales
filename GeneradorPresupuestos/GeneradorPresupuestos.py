#Crea una lista con tamaño dependiente de la cantidad de inputs que ponga el usuario hasta que escriba fin
def crea_lista(): 
    lista = []    
    while(True): 
        val = str(input("Añade un sector de gasto (ej. Comida, Renta, Transporte). Escribe 'fin' para terminar: "))
        if val.lower() == "fin" and len(lista) > 0 : #Verifica si el input es fin y que la lista tenga por lo menos un valor, y termina de registrar datos para la lista
            break
        elif val.lower() == "fin" and len(lista) < 1: #Verifica si el input es fin y que si la lista es menor a 1, de ser asi solicita que añada un sector
            print("Tu lista debe por lo menos tener un sector de gasto incluido. Intente de nuevo")
        elif val.isdigit(): #Verifica si el val de entrada no es un numero
            print("No se aceptan datos numéricos. Intente de nuevo")
        else: #Añade el valor que fue dado por el usuario en la lista, y lo capitaliza
            lista.append(val.lower().capitalize())     
    return lista

#Utiliza la lista creada y solicita valores numericos para añadirlos a una lista con la misma cantidad de posiciones
def futuro_gasto(lista): 
    costo_sector = []
    for i in range(len(lista)):
        while True:
            try: #Corre la solicitud de costo por el usuario
                costo = int(input(f"Cuanto planea gastar en el sector de {lista[i]}: "))
            except: #En caso de que el valor que mando el usuario no sea un int, corre la excepcion y pide que intentne de nuevo
                print("Inserte un valor númerico")
            else: #Si el valor si es integro romple el ciclo while
                break
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
#Si no se llega a utilizar esta funcion el valor default de la lista de porcentajes es None
def porcentajes(lista, costo):
    percent = 0
    suma = 0
    mensajes = []
    listPercent = []
    for s in range(len(costo)):
        suma += costo[s]

    for i in range(len(costo)):
        percent = (costo[i]/suma)*100
        mensaje = f"En el sector {lista[i]} tienes un presupuesto planeado del {percent:.2f}% del total"
        mensajes.append(mensaje)
        listPercent.append(percent)
        
    return mensajes, listPercent #Se devuelve tanto el mensaje para mostrarlo en consola y el valor de porcentaje para añadirlo al registro

#Utilizando la lista numerica y sumando todos los valores de cada posicion, 
# y preguntando las ganancias mensuales se saca una diferencia para verificar si sobra dinero o no
#Si no se llega a utilizar esta funcion el valor default de residuo es None
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
    
    return mensaje, res #Se devuelve tanto el mensaje para mostrarlo en consola y el valor de residuo para añadirlo al registro

#Se guarda la lista de sectores, la lista de costo, la lista de porcentaje y el sobrante dentro de un documento txt de manera que se vea ordenado
def guardaRegistro(lista,costo,porcentaje,sobrante):
    Registro = "Finanzas-Personales-main/GeneradorPresupuestos/Registro.txt" #Ubicacion del archivo Registro.txt acorde a la jerarquia del proyecto
    
    #Si la funcion de porcentaje utiliza su valor defualt, None. Se creara una lista del mismo tamaño que la lista de sectores y añadira la cadena "N/A" 
    if porcentaje is None: 
        porcentaje = []
        for i in range(len(lista)):
            porcentaje.append("N/A")
    #Si la funcion de sobrante utiliza su valor defualt, None. Al final se añadira el mensaje, no se calculo el sobrante
    if sobrante is None:
        sobrante = "No se calculó el sobrante."

    #Abre archivo en modo append para añadir mas contenido al registro
    archivo = open(Registro, "a")

    archivo.write("=== REGISTRO NUEVO ===\n")
    #La segunda linea del archivo pone columnas imaginarias con titulos en cada una con distintas separacions para que este ordenado
    archivo.write(f"{'Sector':15}{'Costo':10}{'Porcentaje %':15}\n")

    #Por cada segmento en la lista de sectores, costo y porcentaje se añade una linea nueva ordenada con las 3 variables
    for i in range(len(lista)):
        #Se fija en si la funcion porcentaje esta usando su estado default, None, o si, si se activo la funcion
        if isinstance(porcentaje[i], (int, float)):
            archivo.write(f"{lista[i]:15}{costo[i]:5}{porcentaje[i]:15.2f}\n") #Añade al archivo el sector, el costo y el porcentaje con 2 decimales
        else:
            archivo.write(f"{lista[i]:15}{costo[i]:5}{porcentaje[i]:>15}\n") ##Añade al archivo el sector, el costo y el porcentaje como cadena "N/A"
            
    archivo.write(f"\nEl sobrante es: ${sobrante}\n\n") #Añade el sobrante al final
    archivo.close()
    print("\nDatos guardados en el registro correctamente")

#Elimina todos los datos guardados previamente en Registro.txt
def borraRegistro(seguro):
    Registro = "Finanzas-Personales-main/GeneradorPresupuestos/Registro.txt" #Ubicacion del archivo Registro.txt acorde a la jerarquia del proyecto
    while True:
        if seguro.lower() == "y":      
            archivo = open(Registro, "w") #Abre el archivo en modo write para sobre escribir todo el archivo
            archivo.write("")#Solo añade un texto vacio al documento
            print("Datos eliminados del registro correctamente")
            archivo.close() 
            break
        elif seguro.lower() == "n":
            print("Volviendo al menu del generador de presupuesto")
            break
        else:
            print("Dato invalido. Volviendo al menu del generador de presupuestos")
            break


#Casos de prueba para todas las funciones
def casos_prueba():
    ganancias = 1000
    sectores = ["Comida", "Salud", "Infraestructura", "Educativo", "Ahorros"]
    costo = [250, 125, 50, 400, 150]
    mensajePor, percent = porcentajes(sectores, costo)
    mensajeSob, res = sobrante(ganancias,costo)
    
    print("INICIANDO CASOS DE PRUEBA \n")

    print("Función de sector_costo: prueba")
    for m in sector_costo(sectores, costo):
        print(m,"\n")

    print("Función de porcentajes: prueba")
    for m in mensajePor:
        print(m ,"\n")

    print("Función de dinero sobrante: prueba")
    print(mensajeSob ,"\n")

    print("Función de guardar registro: prueba")
    guardaRegistro(sectores,costo,percent,res)

    print("\nFuncion de borrar registro: prueba")
    borraRegistro("Y") #Si se le cambia el valor "Y" por "N" el archivo txt si mostrara los casos de prueba de las otras funciones dentro de este

def menu():
    print("\n 1. Imprimir costo por sector actual \n 2. Porcentaje de costo por sector \n " 
    "3. Dinero sobrante \n 4. Guardar cambios \n 5. Borrar registro \n 6. Crear nueva lista \n 7. Casos de prueba \n 8. Salir\n")





