#Simulador de Deudas
#Autor: David Flores Hernandez
#Descripción:Este programa permite simular el pago de una deuda en distintos plazos y con distintas tasas de interés.
#El usuario ingresa el monto de la deuda, la tasa de interés anual y el plazo en meses.
#El sistema calcula el monto de las cuotas mensuales y quincenales, y muestra cómo varían dependiendo del plazo.




def calcular_cuota_mensual(monto, interes_anual, meses):
    
    #Calcula la cuota mensual de una deuda
    #monto (float): cantidad total de la deuda
    #interes_anual (float): tasa de interés anual (en %)
    #meses (int): número de meses del plazo
    
    interes_mensual = interes_anual / 12 / 100

    # Si no hay interés, simplemente divide el monto entre los meses
    if interes_mensual == 0:
        pago = monto / meses
    else:
        # Fórmula para calcular el pago mensual de un préstamo con interés compuesto
        pago = monto * (interes_mensual * (1 + interes_mensual) ** meses) / ((1 + interes_mensual) ** meses - 1)
    
    return pago



def crear_tabla_pagos(monto, interes_anual, meses):
    
    # Función para crear una tabla con los pagos mensuales y quincenales
    
    tabla = []

    # Recorre cada mes del plazo
    for mes in range(1, meses + 1):
        # Calcula el pago mensual para ese mes
        pago_mes = calcular_cuota_mensual(monto, interes_anual, meses)
        # Calcula el pago quincenal 
        pago_quincena = pago_mes / 2
        fila = [mes, pago_mes, pago_quincena]
        tabla.append(fila)
    
    # Retorna la tabla completa con todos los pagos
    return tabla



def mostrar_tabla(tabla):
    
    # Función para mostrar la tabla de pagos en pantalla
    
    print("--------------Tabla de simulación--------------")
    print(f"{'Mes'} | {'Pago Mensual'} | {'Pago Quincenal'}")
    print("-----------------------------------------------")

    # Recorre cada fila de la tabla y muestra los datos formateados
    for fila in tabla:
        mes = fila[0]
        pago_mensual = fila[1]
        pago_quincenal = fila[2]
        # Muestra los valores con 2 decimales
        print(f"{mes} | ${pago_mensual:.2f} | ${pago_quincenal:.2f}")





    print("Simulador de Deudas")

    # Solicita al usuario los datos de la deuda
    monto = float(input("Dame el monto de la deuda: "))
    interes_anual = float(input("Dame el interes anual: "))
    meses = int(input("Dame el plazo en meses: "))

    # Genera y muestra la tabla de pagos
    tabla_pagos = crear_tabla_pagos(monto, interes_anual, meses)
    mostrar_tabla(tabla_pagos)

    # Pregunta si el usuario quiere realizar otra simulación
    continuar = str(input("¿Deseas continuar? "))
    



def pruebas():
    print("Pruebas automáticas")     
    assert calcular_cuota_mensual(1200, 0, 12) == 100          #Prueba 1: sin interés (cuota mensual debe ser monto / meses)    

    cuota_mensual = calcular_cuota_mensual(1200, 0, 12)
    cuota_quincenal = cuota_mensual / 2                        #Prueba 2: cuota quincenal es la mitad de la mensual
    assert cuota_quincenal == 50    

    assert calcular_cuota_mensual(1, 0, 1) == 1                #Prueba 3: valores extremos (monto = 1, 1 mes, sin interés)
             
    print("Todas las pruebas pasaron correctamente.\n")
    


pruebas()

    
 




