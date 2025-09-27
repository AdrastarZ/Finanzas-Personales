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
    if interes_mensual == 0:
        return monto / meses
    cuota = monto * (interes_mensual * (1 + interes_mensual ) ** meses) / ((1 + interes_mensual) ** meses -1)
    return cuota

def calcular_cuota_quincenal(monto, interes_anual, meses):
    
    quincenas = meses * 2
    interes_quincenal = interes_anual / 24 / 100
    if interes_quincenal == 0:
        return monto / quincenas
    cuota = monto * (interes_quincenal * (1 + interes_quincenal) ** quincenas) / ((1 + interes_quincenal) ** quincenas - 1)
    return cuota


def mostrar_escenarios(monto, interes, meses):
    
    print("Escenarios de pago:")
    for plazo in range(6, meses +1, 6):
        cuota_mensual = calcular_cuota_mensual(monto, interes, plazo)
        cuota_quincenal = calcular_cuota_quincenal(monto, interes, plazo)
        
        print("Plazo de", plazo, "meses")
        print("Pago mensual: ", round(cuota_mensual, 2))
        print("Pago quincenal: ", round(cuota_quincenal, 2))
        
        
        
def pruebas():
    
    print("Pruebas automáticas")     

    assert calcular_cuota_mensual(1200, 0, 12) == 100     # Caso 1: sin interés
    assert calcular_cuota_quincenal(1200, 0, 12) == 50    # Caso 2: sin interés quincenal
    assert calcular_cuota_mensual(1, 0, 1) == 1           # Caso 3: valores extremos
    print("Todas las pruebas pasaron correctamente.\n")
    
    
def main():
    
    print("Simulador de Deudas")
    
    monto = float(input("Dame el monto de las deudas: "))
    interes = float(input("Dame el interés anual en %: "))
    meses = int(input("Dame  plazo en meses: "))
    
    mostrar_escenarios(monto, interes, meses)
    
main()
    
    
    
    
        
        
        












