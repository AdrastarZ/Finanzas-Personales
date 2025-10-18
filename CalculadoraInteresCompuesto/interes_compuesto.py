#Entrega de proyecto
#Proyecto Interés Compuesto
# AA_GOIP
# Fecha: 17/10/2025
# Función: Conversión de unidades (anuales y mensuales)
def convertir_unidades(interes, tipo_tasa, periodos, tipo_periodo):#  Esta función convierte los valores de tasa e intervalos de tiempo,dependiendo si se trabaja en formato anual (A) o mensual (M). para que no sea valida alguna otra opción

    # Validación con while para que el usuario no pueda poner otra letra
    while tipo_tasa not in ["A", "M"]:
        tipo_tasa = input("Tasa inválida. Por favor ingresa 'A' para anual o 'M' para mensual: ").upper()
    while tipo_periodo not in ["A", "M"]:
        tipo_periodo = input("Periodo inválido. Por favor ingresa 'A' para años o 'M' para meses: ").upper()

    if tipo_tasa == "A" and tipo_periodo == "M":
        interes = interes / 12 # Si la tasa es anual y los periodos están en meses, se divide entre 12
        print("Se ha convertido la tasa anual a mensual para mantener la coherencia de unidades.")
    elif tipo_tasa == "M" and tipo_periodo == "A":
        periodos = periodos * 12  # Si la tasa es mensual y los periodos están en años, se multiplican por 12
        print("Se han convertido los periodos de años a meses.")
    else:
        print("No fue necesario hacer ninguna conversión.") # Si ambas unidades coinciden, no se modifica nada.

    # Se retornan los nuevos valores para usarse en los calculos que faltan
    return interes, periodos

# Función: Préstamos con interés compuesto
def prestamocompuestas(dineropedido, interes, periodos, frecuencia="M"):# Esta función calcula el monto total a pagar y el pago por periodo,  aplicando la fórmula de interés compuesto.
    monto = dineropedido * (1 + interes)**periodos # Se calcula el monto final usando la fórmula 
    if frecuencia == "M":  # Dependiendo de la frecuencia de pago, se determina el número de pagos totales
        pagos = periodos * 12  # si son pagos mensuales
    else:
        pagos = periodos       # si son pagos anuales
    pagoperiodo = monto / pagos # Se obtiene el pago por periodo dividiendo el total entre los pagos
    matriz_amortizacion = [] # Se construye una tabla con los primeros 5 periodos para mostrar la evolución
    for i in range(1, min(6, pagos + 1)):  # el for genera una lista con los pagos iniciales
        pago = dineropedido * (1 + interes)**(i*(periodos/pagos)) / i  # Cálculo aproximado del pago en cada iteración 
        matriz_amortizacion.append([i, round(pago, 2)])  # se guarda el número de pago del usuario
    print("\nTabla de amortización de los primeros 5 pagos:") 
    print("Periodo | Pago")
    for fila in matriz_amortizacion:
        print(f"{fila[0]:>6} | {fila[1]:>8.2f}")
    return monto, pagoperiodo  # Retorna el monto total y el pago por periodo para usarlos en el menú

# Función: Inversión con interés compuesto
def inversionescompuestas(inversion, interes, periodos, frecuencia="A"):#Esta función calcula el crecimiento de una inversión con interés compuesto, tanto si se reinvierte (interés compuesto) como si se retira (interés simple).
    monto_compuesto = inversion * (1 + interes)**periodos# Calculo de inversión compuesta (reinvirtiendo los intereses)
    ganancia_compuesta = monto_compuesto - inversion
    ganancia_retirada = inversion * interes * periodos# Cálculo de inversión sin reinversión (interés simple)
    monto_retirado = inversion + ganancia_retirada
    tabla_inversion = [] # Se construye una tabla con los primeros 5 periodos para mostrar la evolución
    for i in range(1, min(6, periodos + 1)):
        valor_acumulado = inversion * (1 + interes)**i
        ganancia = valor_acumulado - inversion
        tabla_inversion.append([i, round(valor_acumulado, 2), round(ganancia, 2)])
    print("\nTabla de evolución de inversión (primeros 5 periodos):")
    print("Periodo | Valor acumulado | Ganancia")
    for fila in tabla_inversion:
        print(f"{fila[0]:>6} | {fila[1]:>15.2f} | {fila[2]:>8.2f}")
    return monto_compuesto, ganancia_compuesta, monto_retirado, ganancia_retirada 

# Menú de la calculadora de interés compuesto
def menu_Calculadora():#Esta función despliega el menú principal de la calculadora de interés compuesto, Desde aquí el usuario puede elegir si desea hacer cálculos de préstamos o inversiones.
    print("Bienvenido a la calculadora de interés compuesto :) ")
    print("Menú principal")
    print("1. Calculadora de interés compuesto para Préstamos")
    print("2. Calculadora de interés compuesto para Inversiones")
    print("3. Mostrar historial de operaciones")
    print("4. Salir de la calculadora de interés compuesto")

