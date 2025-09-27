#Entrega de proyecto
#Proyecto Interés Compuesto
#AA_GOIP
#fecha: 24/09/2025

# Conversión de unidades (anuales y mensuales)
def convertir_unidades(interes, tipo_tasa, periodos, tipo_periodo):# la primera funcion ayuda a convertir las unidades "n" para que el rocedimiento sea correcto ya que si la tasa es anual y el tipo de periodo es semestral, tenen timpos distintos por ende estaría mal el procedimiento.
    if tipo_tasa == "A" and tipo_periodo == "M": # el if define dos parámetros si es la tasa y el tipo de periodos es anual o semestral para hacer la conversion correcta 
        interes = interes / 12      # anual -mensual
    elif tipo_tasa == "M" and tipo_periodo == "A":#el elif define si se hará la conversión ahora de manera inversa
        periodos = periodos * 12    # meses - años
    return interes, periodos #se regresa el valor a el int del interes y periodos para que despues se  mande aajecutar el print


# Préstamos con interés compuesto
def prestamocompuestas(dineropedido, interes, periodos, frecuencia="M"):# la segunda función es la encargada de la opción de interés compuesto en los prestamos o deudas 
    monto = dineropedido * (1 + interes)**periodos #la opereación del interés compuesto, esto ocurre después del parametro del if para que tanto n como i tengan la misma conversión de tiempo
    if frecuencia == "M":   # pagos mensuales
        pagos = periodos * 12 #operación
    else:                   # pagos anuales
        pagos = periodos # sin operación ya que lo saca de manera directa.
    pagoperiodo = monto / pagos # solo se divide para que que de la opcion individual
    return monto, pagoperiodo #se regresa el valor a el int del prestamocompuesto para que se despliegue con los print


# Inversión con interés compuesto
def inversionescompuestas(inversion, interes, periodos, frecuencia="A"): # La tercera función es la encargada de las inversiones de interes compuesto 
    monto_compuesto = inversion * (1 + interes)**periodos # la ooperación de interés compuesto, ocurre despues del paraá metro de los if para que n e i tengan el mismo tiempo marcado
    ganancia_compuesta = monto_compuesto - inversion #se da el total de la ganancia sin contar lo que se invirtió

    ganancia_retirada = inversion * interes * periodos # la segunda operación es si la inversión se retirá periodicamente 
    monto_retirado = inversion + ganancia_retirada #se da cuanto es el monto que podrá retirar de acuero al periodo

    return monto_compuesto, ganancia_compuesta, monto_retirado, ganancia_retirada # se regresa el valor a el int de las inversiones compuestas para que se despliegue con su respectivo print


# Menú de la calculadora de interes compuesto
def menu(): #La cuarta función se definirá como el menú principal de mi sección 
    print("Bienvenido a la calculadora de interés compuesto :) ")#se despliegan los mensajes
    print("Menú principal")
    print("1. Calculadora de interés compuesto para Préstamos")#se despliega el mensaje que va a ir conectado con el while true
    print("2. Calculadora de interés compuesto para Inversiones") 
    print("3. Salir de la calculadora de interés compuesto")


# La función main que controla el código
def main():
    while True:
        menu()
        opcion = input("Por favor selecciona una opción de forma numérica: ")# se le pide al usuario que seleccione una opción de mnera numérica para que el código siga 

        if opcion == "1":
            dineropedido = float(input("Ingresa la cantidad solicitada: ")) #Se le pide al usuario que anexe la cantidad que pedira como el prestamo
            interes = float(input("Ingresa la tasa de interés (%): "))/100 #se divide entre 100 por ser una cantidad en porcentaje para que pase para la función
            tipo_tasa = input("¿La tasa es Anual (A) o Mensual (M)? ").upper() #Se le agrega el punto upper en caso de que la opcion que me den sea minuscula para que el codigo aun pueda contarlo
            periodos = int(input("Ingresa el número de periodos: "))
            tipo_periodo = input("¿Los periodos están en Años (A) o Meses (M)? ").upper()#Se le agrega el punto upper en caso de que la opcion que me den sea minuscula para que el codigo aun pueda contarlo
            frecuencia = input("¿Los pagos son Mensuales (M) o Anuales (A)? ").upper()#Se le agrega el punto upper en caso de que la opcion que me den sea minuscula para que el codigo aun pueda contarlo

            interes, periodos = convertir_unidades(interes, tipo_tasa, periodos, tipo_periodo) # se llaman las funciones que hacen las operaciones 
            monto, pagoperiodo = prestamocompuestas(dineropedido, interes, periodos, frecuencia)

            print("\n--- Resultados del préstamo ---")# para separarlo de lo escrito 
            print(f"Monto total a pagar: {monto:.2f}")# A el monto se le pone el parámetro para que solo se le agreguen 2 puntos decimales 
            print(f"Pago por periodo ({frecuencia}): {pagoperiodo:.2f}") # se imprime el pago por periodo con 2 puntos decimales 

        elif opcion == "2":
            inversion = float(input("Ingresa la inversión inicial: ")) # se le pie al usuario que anexe el valor de la inversión
            interes = float(input("Ingresa la tasa de interés (%): "))/100 #se divide entre 100 por ser una cantidad en porcentaje para que pase para la función
            tipo_tasa = input("¿La tasa es Anual (A) o Mensual (M)? ").upper()#Se le agrega el punto upper en caso de que la opcion que me den sea minuscula para que el codigo aun pueda contarlo
            periodos = int(input("Ingresa el número de periodos: ")) #Se le pide al usuario el numero de periodos que le dieron en la oferta de inversión
            tipo_periodo = input("¿Los periodos están en Años (A) o Meses (M)? ").upper()#Se le agrega el punto upper en caso de que la opcion que me den sea minuscula para que el codigo aun pueda contarlo
            frecuencia = input("¿Retirarás la inversión de manera Mensual (M) o Anual (A)? ").upper()#Se le agrega el punto upper en caso de que la opcion que me den sea minuscula para que el codigo aun pueda contarlo

            interes, periodos = convertir_unidades(interes, tipo_tasa, periodos, tipo_periodo)# se llama a las funciones que hacen las operaciones 
            monto_compuesto, ganancia_compuesta, monto_retirado, ganancia_retirada = inversionescompuestas(inversion, interes, periodos, frecuencia)

            print("\n--- Resultados de la inversión ---")# Se despliega el mensaje final se le pone "n" para separarlo de lo escrito 
            print(f"Con reinversión (interés compuesto): Monto final = {monto_compuesto:.2f}, Ganancia = {ganancia_compuesta:.2f}") #se le ponen dos puntos decimales
            print(f"Sin reinversión (retiro periódico): Monto final = {monto_retirado:.2f}, Ganancia = {ganancia_retirada:.2f}") #Se le ponen dos puntos decimales 

        elif opcion == "3": # la opción para romper el ciclo
            print("Gracias por utilizar la calculadora de Interés Compuesto")#se despliegan los mensajes 
            break #se rompe el ciclo

        else: # El último parámetro
            print("Opción no válida, intentalo de nuevo.") # por si escribe algo que no va conforma a las preguntas
main() # el main que guarda la información
