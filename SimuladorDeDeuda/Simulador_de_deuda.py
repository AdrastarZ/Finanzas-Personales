#Simulador de Deudas
#Descripción:Este programa permite simular el pago de una deuda en distintos plazos y con distintas tasas de interés.
#El usuario ingresa el monto de la deuda, la tasa de interés anual y el plazo en meses.
#El sistema calcula el monto de las cuotas mensuales y quincenales, y muestra cómo varían dependiendo del plazo.


def calcular_cuota_mensual(monto, interes_anual, meses):
    
    #Función que calcula la cuota mensual de una deuda

    interes_mensual = interes_anual / 12 / 100  #Convierte el interés anual a mensual
    
    if monto <= 0 or interes_anual < 0:
        return str(f"Los datos que me diste no son validos: monto {monto}, interes anual {interes_anual}")
    
    elif interes_mensual == 0:
        return monto / meses    #Si no hay interés, divide la deuda en partes iguales
    
    else:
        cuota = monto * (interes_mensual * (1 + interes_mensual) ** meses) / ((1 + interes_mensual) ** meses - 1)   #Formula del pago fijo mensual
        return cuota


def calcular_cuota_quincenal(monto, interes_anual, meses):
    
    #Función que calcula la cuota quincenal
    
    quincenas = meses * 2       #Convierte meses a quincenas
    interes_quincenal = interes_anual / 24 / 100    #Convierte interés anual a quincenal
    
    if monto <= 0 or interes_anual < 0:
        return str(f"Los datos que me diste no son validos: monto {monto}, interes anual {interes_anual}")
    
    elif interes_quincenal == 0:
        return monto / quincenas
    
    else:
        cuota = monto * (interes_quincenal * (1 + interes_quincenal) ** quincenas) / ((1 + interes_quincenal) ** quincenas - 1)
        return cuota
 
  
def calcular_interes_total_mensual(monto, interes, meses):
    
    #Calcula el interés total pagado en pagos mensuales
    
    total = calcular_cuota_mensual(monto, interes, meses)
    
    if type(total) == str:
        return total
    
    total_pagado = total * meses
    intereses = total_pagado - monto  #Resta el total menos la deuda para obtener el interés total
    
    return intereses


def calcular_interes_total_quincenal(monto, interes, meses):
    
    # Calcula el interés total pagado en pagos quincenales

    total = calcular_cuota_quincenal(monto, interes, meses)
    
    if type(total) == str:
        return total
    
    total_pagado = total * (meses * 2)
    intereses = total_pagado - monto    #Resta el total menos la deuda para obtener el interés total
    
    return intereses


def calcular_escenarios(monto, interes, meses):
    
    #Crea diferentes escenarios con distintos plazos
 
    cuotas = []
    
    for plazo in range(1, meses +1):
        cuota_mensual = calcular_cuota_mensual(monto, interes, plazo)
        cuota_quincenal = calcular_cuota_quincenal(monto, interes, plazo)
        
        if type(cuota_mensual) == str:
            return cuota_mensual
        
        cuotas.append([plazo, cuota_quincenal, cuota_mensual])
        
    return cuotas    #Regresa las listas con escenarios


def calcular_total_pagar(monto, interes, meses):
    
    #Calcula los totales a pagar tanto mensuales como quincenales para cada plazo
    
    totales = []
    
    for plazo in range(1, meses + 1):
        cuota_mensual = calcular_cuota_mensual(monto, interes, plazo)
        cuota_quincenal = calcular_cuota_quincenal(monto, interes, plazo)
        
        if type(cuota_mensual) == str:
            return cuota_mensual
        
        total_mensual = cuota_mensual * plazo
        total_quincenal = cuota_quincenal * (plazo * 2)
        totales.append([plazo, total_quincenal, total_mensual])
        
    return totales


def guardar_escenarios(monto, interes, meses):
    
    #Guarda los escenarios en un archivo

    escenarios = calcular_escenarios(monto, interes, meses)
    
    with open('escenarios_deuda.csv', 'w') as file:
        file.write('Plazo,Cuota Quincenal,Cuota Mensual\n')
        
        for plazo, quincenal, mensual in escenarios:
            file.write(f'{plazo},{quincenal:.2f},{mensual:.2f}\n')
            
    return "\nEscenarios guardados en archivo escenarios_deuda.csv"


def guardar_totales(monto, interes, meses):
    
    #Guarda los totales de pago en un archivo 
    
    totales = calcular_total_pagar(monto, interes, meses)
    
    with open('totales_deuda.csv', 'w') as file:
        file.write('Plazo,Total Quincenal,Total Mensual')
        
        for plazo, quincenal, mensual in totales:
            file.write(f'{plazo},{quincenal:.2f},{mensual:.2f}\n')
            
    return "\nTotales guardados en archivo totales_deuda.csv"


def pedir_datos():
    
    #Pide los adtos al usuario
    
    monto = float(input("Dame el monto de las deudas: "))
    interes = float(input("Dame el interés anual en %: "))
    meses = int(input("Dame el plazo en meses: "))
    
    return monto, interes, meses


def pruebas():
    
    #Se hacen varios casos de prueba para compromar que el codigo funciona de manera correcta
    
    esperado_mensual_no_interes = 100
    calculado_mensual_no_interes = calcular_cuota_mensual(1200, 0, 12)
    assert esperado_mensual_no_interes == calculado_mensual_no_interes
    
    
    #Prueba con interés negativo (debe devolver mensaje de error)

    esperado_quincenal_no_interes = 50
    calculado_quincenal_no_interes = calcular_cuota_quincenal(1200, 0, 12)
    assert esperado_quincenal_no_interes == calculado_quincenal_no_interes
    

    esperado_mensual_interes_negativo = "Los datos que me diste no son validos: monto 1200, interes anual -1"
    calculado_mensual_interes_negativo = calcular_cuota_mensual(1200, -1, 6)
    assert esperado_mensual_interes_negativo == calculado_mensual_interes_negativo
    

    esperado_quincenal_interes_negativo = "Los datos que me diste no son validos: monto 1200, interes anual -1"
    calculado_quincenal_interes_negativo = calcular_cuota_quincenal(1200, -1, 6)
    assert esperado_quincenal_interes_negativo == calculado_quincenal_interes_negativo
    

    esperado_mensual_interes = 205.87
    calculado_mensual_interes = calcular_cuota_mensual(1200, 10, 6)
    calculado_mensual_interes_redondeado = round(calculado_mensual_interes, 2)
    assert esperado_mensual_interes == calculado_mensual_interes_redondeado
    

    esperado_quincenal_interes = 102.73
    calculado_quincenal_interes = calcular_cuota_quincenal(1200, 10, 6)
    calculado_quincenal_interes_redondeado = round(calculado_quincenal_interes, 2)
    assert esperado_quincenal_interes == calculado_quincenal_interes_redondeado
    

    escenarios = calcular_escenarios(1200, 0, 2)
    assert len(escenarios) == 2
    assert escenarios[0][0] == 1
    assert escenarios[1][0] == 2
    assert escenarios[0][2] == 1200
    assert escenarios[1][2] == 600
    

    totales = calcular_total_pagar(1200, 0, 2)
    assert len(totales) == 2
    assert totales[0][0] == 1
    assert totales[1][0] == 2
    assert totales[0][2] == 1200
    assert totales[1][2] == 1200
    

    esperado_interes_mensual = 66.19
    calculado_interes_mensual = calcular_interes_total_mensual(1000, 12, 12)
    calculado_interes_mensual_redondeado = round(calculado_interes_mensual, 2)
    assert esperado_interes_mensual == calculado_interes_mensual_redondeado
    

    esperado_interes_quincenal = 63.69
    calculado_interes_quincenal = calcular_interes_total_quincenal(1000, 12, 12)
    calculado_interes_quincenal_redondeado = round(calculado_interes_quincenal, 2)
    assert esperado_interes_quincenal == calculado_interes_quincenal_redondeado
    

    return "\nTodas las pruebas pasaron correctamente"


