from GestorGastos import Gestor_de_gastos
from CalculadoraInteresCompuesto import interes_compuesto
from GeneradorPresupuestos import GeneradorPresupuestos as GP
from SimuladorDeDeuda import Simulador_de_deuda as SD
#Listas para guardar historial de operaciones 
historial_prestamos = [] # se guardarán los datos de los préstamos realizados
historial_inversiones = [] # se guardarán los datos de las inversiones realizadas
def main():
    activo = True  # variable que mantiene activo el programa hasta que el usuario decida salir
    while activo:
        print("\nMENÚ PRINCIPAL")
        print("Bienvenido al apartado de FINANZAS PERSONALES :) ")
        print("1. Calculadora de interés compuesto")
        print("2. Generador de presupuestos")
        print("3. Gestor de gastos")
        print("4. Simulador de deuda")
        print("5. Salir")
        codigo = input("Elige una de las opciones: ")

        if codigo =="1":
              while True:
                interes_compuesto.menu_Calculadora()
                opcion = input("Por favor selecciona una opción de forma numérica: ")
                
                if opcion == "1":
                    dineropedido = float(input("Ingresa la cantidad solicitada: ")) #Se le pide al usuario que anexe la cantidad que pedira como el prestamo
                    interes = float(input("Ingresa la tasa de interés (%): "))/100 #se divide entre 100 por ser una cantidad en porcentaje para que pase para la función
                    tipo_tasa = input("¿La tasa es Anual (A) o Mensual (M)? ").upper() #Se le agrega el punto upper en caso de que la opcion que me den sea minuscula para que el codigo aun pueda contarlo
                    periodos = int(input("Ingresa el número de periodos: "))
                    tipo_periodo = input("¿Los periodos están en Años (A) o Meses (M)? ").upper()#Se le agrega el punto upper en caso de que la opcion que me den sea minuscula para que el codigo aun pueda contarlo
                    frecuencia = input("¿Los pagos son Mensuales (M) o Anuales (A)? ").upper()#Se le agrega el punto upper en caso de que la opcion que me den sea minuscula para que el codigo aun pueda contarlo

                    interes, periodos = interes_compuesto.convertir_unidades(interes, tipo_tasa, periodos, tipo_periodo) # se llaman las funciones que hacen las operaciones 
                    monto, pagoperiodo = interes_compuesto.prestamocompuestas(dineropedido, interes, periodos, frecuencia)

                    print("Resultados del préstamo")# para separarlo de lo escrito 
                    print(f"Monto total a pagar: {monto:.2f}")# A el monto se le pone el parámetro para que solo se le agreguen 2 puntos decimales 
                    print(f"Pago por periodo ({frecuencia}): {pagoperiodo:.2f}") # se imprime el pago por periodo con 2 puntos decimales 

                    # se agrega el registro al historial de préstamos
                    historial_prestamos.append({
                    "Cantidad": dineropedido,
                    "Interés": interes,
                    "Periodos": periodos,
                    "Monto total": monto,
                    "Pago por periodo": pagoperiodo,
                    "Frecuencia": frecuencia
                    })

                elif opcion == "2":
                    inversion = float(input("Ingresa la inversión inicial: ")) # se le pie al usuario que anexe el valor de la inversión
                    interes = float(input("Ingresa la tasa de interés (%): "))/100 #se divide entre 100 por ser una cantidad en porcentaje para que pase para la función
                    tipo_tasa = input("¿La tasa es Anual (A) o Mensual (M)? ").upper()#Se le agrega el punto upper en caso de que la opcion que me den sea minuscula para que el codigo aun pueda contarlo
                    periodos = int(input("Ingresa el número de periodos: ")) #Se le pide al usuario el numero de periodos que le dieron en la oferta de inversión
                    tipo_periodo = input("¿Los periodos están en Años (A) o Meses (M)? ").upper()#Se le agrega el punto upper en caso de que la opcion que me den sea minuscula para que el codigo aun pueda contarlo
                    frecuencia = input("¿Retirarás la inversión de manera Mensual (M) o Anual (A)? ").upper()#Se le agrega el punto upper en caso de que la opcion que me den sea minuscula para que el codigo aun pueda contarlo

                    interes, periodos = interes_compuesto.convertir_unidades(interes, tipo_tasa, periodos, tipo_periodo)# se llama a las funciones que hacen las operaciones 
                    monto_compuesto, ganancia_compuesta, monto_retirado, ganancia_retirada = interes_compuesto.inversionescompuestas(inversion, interes, periodos, frecuencia)

                    print("Resultados de la inversión")# Se despliega el mensaje final se le pone "n" para separarlo de lo escrito 
                    print(f"Con reinversión (interés compuesto): Monto final = {monto_compuesto:.2f}, Ganancia = {ganancia_compuesta:.2f}") #se le ponen dos puntos decimales
                    print(f"Sin reinversión (retiro periódico): Monto final = {monto_retirado:.2f}, Ganancia = {ganancia_retirada:.2f}") #Se le ponen dos puntos decimales 

                    # se agrega el registro al historial de inversiones
                    historial_inversiones.append({
                    "Inversión": inversion,
                    "Interés": interes,
                    "Periodos": periodos,
                    "Monto compuesto": monto_compuesto,
                    "Ganancia compuesta": ganancia_compuesta,
                    "Frecuencia": frecuencia
                    })

                elif opcion == "3": #muestra el historial completo
                    print("\nHISTORIAL DE OPERACIONES")
                    if historial_prestamos: # se muestra el historial de préstamos
                        print("\nHistorial de préstamos:")
                    for p in historial_prestamos:
                        print(p)
                    else:
                        print("\nNo se han realizado préstamos aún.")

                    if historial_inversiones: # se muestra el historial de inversiones
                        print("\nHistorial de inversiones:")
                    for i in historial_inversiones:
                        print(i)
                    else:
                        print("\nNo se han realizado inversiones aún.")
            
                elif opcion == "4": # la opción para romper el ciclo
                    print("Gracias por utilizar la calculadora de Interés Compuesto :) ")#se despliegan los mensajes 
                    break #se rompe el ciclo

                else: # El último parámetro
                    print("Opción no válida, intentalo de nuevo.") # por si escribe algo que no va conforma a las preguntas

        if codigo =="2":
            porcentaje = None
            sobrante = None
            opcionesGenPres = 0

            print("\nBienvenido a tu Generador de Presupuesto personal")
            print("Empecemos creando tu lista con los sectores donde tienes planeado gastar")
            lista = GP.crea_lista()
            print("Ahora añade el costo previsto que tendra cada sector ")
            costo = GP.futuro_gasto(lista)

            while True:
                GP.menu()
                opcionesGenPres = int(input("Seleccione un numero del menu para continuar con el proceso: "))
                if(opcionesGenPres == 1):
                    for m in GP.sector_costo(lista, costo): #Para que cada lista salga ordenada se aplica un for para cada funcion
                        print(m)

                elif(opcionesGenPres == 2):
                    mensajePor, porcentaje = GP.porcentajes(lista, costo)
                    for m in mensajePor:#Para que cada lista salga ordenada se aplica un for para cada funcion
                        print(m)
                      
                elif(opcionesGenPres == 3):
                    ganancias = int(input("¿Cuanto ganas mensualmente? "))
                    mensajeSob, sobrante = GP.sobrante(ganancias,costo)
                    print(mensajeSob)
                    
                elif(opcionesGenPres == 4):
                    GP.guardaRegistro(lista, costo, porcentaje, sobrante)
                    
                elif(opcionesGenPres == 5):
                    seguro = str(input("Estas seguro que quieres borrar los datos de tu Registro? Esta acción NO es reversible (Y/N) "))
                    GP.borraRegistro(seguro)     
                        
                elif(opcionesGenPres == 6):
                    while True:
                        nuevaVieja = input("Estas seguro que quieres crear una nueva lista? Los valores anterirores que hayas anotado seran eliminados (Y/N) ")
                        if nuevaVieja.lower() == "y":
                            sobrante = None
                            porcentaje = None
                            lista = GP.crea_lista()
                            print("Ahora añade el costo previsto que tendra cada sector ")
                            costo = GP.futuro_gasto(lista)
                            break
                        elif nuevaVieja == "n":
                            break
                        else: 
                            print("Opción no valida, por favor intente de nuevo")

                elif(opcionesGenPres == 7):
                    GP.casos_prueba()

                elif(opcionesGenPres == 8):
                    print("\nSaliendo de la sesión.  \n"
                    "Gracias por usar el generador de presupuesto :) \n")
                    break
                else:
                    print("\nOpción no valida. Intente de nuevo\n")
                    
        elif codigo == "3":  
            while True:  # comportamiento cíclico
                opcion = Gestor_de_gastos.menu()
                if opcion == "1":
                    Gestor_de_gastos.registrar_movimiento("ingreso")
                elif opcion == "2":
                    Gestor_de_gastos.registrar_movimiento("egreso")
                elif opcion == "3":
                    Gestor_de_gastos.mostrar_resumen()
                elif opcion == "4":
                    Gestor_de_gastos.establecer_presupuesto()
                elif opcion == "5":
                    Gestor_de_gastos.establecer_meta()
                elif opcion == "6":
                    Gestor_de_gastos.caso_prueba_demo()
                elif opcion == "7":
                    print("¡Hasta luego!")
                    break
                else:
                    print("Opción inválida. Intenta de nuevo.")
            
        elif codigo == "4":
            monto, interes, meses = SD.pedir_datos()
            while True:
                print("\n----------- MENÚ PARA SIMULADOR DE DEUDA -----------")
                print("\nSeleccione la opción de la consulta que quiere hacer\n")
                print("Opción 1: Calcular la cuota mensual")
                print("Opción 2: Calcular la cuota quincenal")
                print("Opción 3: Calcular escenarios mensual/quincenal")
                print("Opción 4: Calcular el total a pagar")
                print("Opción 5: Calcular intereses totales en plan mensual")
                print("Opción 6: Calcular intereses totales en plan quincenal")
                print("Opción 7: Guardar escenarios en un archivo")
                print("Opción 8: Guardar totales en un archivo")
                print("Opción 9: Correr pruebas")
                print("Opción 10: Salir")
                opcion = int(input("\nOpción a seleccionar: "))
                if opcion == 1:
                    cuota_mensual = SD.calcular_cuota_mensual(monto, interes, meses)
                    print(f"\nLa cuota mensual sería: {cuota_mensual:.2f}\n")
                elif opcion == 2:
                    cuota_quincenal = SD.calcular_cuota_quincenal(monto, interes, meses)
                    print(f"\nLa cuota quincenal sería: {cuota_quincenal:.2f}\n")
                elif opcion == 3:
                    escenarios = SD.calcular_escenarios(monto, interes, meses)
                    print(f"\n------------------ Tabla de escenarios ------------------")
                    for fila in escenarios:
                        plazo, quincenal, mensual = fila
                        print(f"Plazo: {plazo} | Pago quincenal: {quincenal:.2f} | Pago mensual: {mensual:.2f}")
                elif opcion == 4:
                    total_pagar = SD.calcular_total_pagar(monto, interes, meses)
                    print(f"\n------------------ Tabla de totales ------------------")
                    for fila in total_pagar:
                        plazo, quincenal, mensual = fila
                        print(f"Plazo: {plazo} | Total quincenal: {quincenal:.2f} | Total mensual: {mensual:.2f}")
                elif opcion == 5:
                    interes_mensual = SD.calcular_interes_total_mensual(monto, interes, meses)
                    print(f"\nEl interés total a pagar en este plazo es de {interes_mensual:.2f} pesos\n")
                elif opcion == 6:
                    interes_quincenal = SD.calcular_interes_total_quincenal(monto, interes, meses)
                    print(f"\nEl interés total a pagar en este plazo es de {interes_quincenal:.2f} pesos\n")
                elif opcion == 7:
                    print("\nGuardando escenarios en un archivo")
                    guardado_escenarios = SD.guardar_escenarios(monto, interes, meses)
                    print(guardado_escenarios)
                elif opcion == 8:
                    print("\nGuardando totales en un archivo")
                    guardado_totales = SD.guardar_totales(monto, interes, meses)
                    print(guardado_totales)
                elif opcion == 9:
                    resultados = SD.pruebas()
                    print(resultados)
                elif opcion == 10:
                    print("\nSaliendo del simulador de deuda")
                    break
                else:
                    print("\nSelecciona una opción válida")
        
        elif codigo =="5":
            print("Saliendo del programa, gracias :) ")
            activo = False # se cambia a False para terminar el programa
            break # se rompe el ciclo principal
        else:
            print("opcion no válida. Intentalo de nuevo.")
if __name__ == "__main__":
    main() 





 
