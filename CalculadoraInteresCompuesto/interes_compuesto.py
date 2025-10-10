#Entrega de proyecto
#Proyecto Interés Compuesto
#AA_GOIP
#fecha: 24/09/2025
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
def menu_Calculadora(): #La cuarta función se definirá como el menú principal de mi sección 
    print("Bienvenido a la calculadora de interés compuesto :) ")#se despliegan los mensajes
    print("Menú principal")
    print("1. Calculadora de interés compuesto para Préstamos")#se despliega el mensaje que va a ir conectado con el while true
    print("2. Calculadora de interés compuesto para Inversiones") 
    print("3.Mostrar historial de operaciones" )
    print("4. Salir de la calculadora de interés compuesto") #se agrega una nueva opción para ver los registros realizados
