from GestorGastos.Gestor_de_gastos import gestor_de_gastos
from CalculadoraInteresCompuesto import interes_compuesto

def main():
    while True:
        print("\nMENÚ PRINCIPAL")
        print("Bienvenido al apartado de FINANZAS PERSONALES :) ")
        print("1. Calculadora de interés compuesto")
        print("2. Generador de presupuestos")
        print("3. Gestor de gastos")
        print("4. Simulador de deuda")
        print("5. Salir")
        opcion = input("Elige una de las opciones: ")

        if opcion =="1":
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

                elif opcion == "3": # nueva opción para mostrar el historial completo
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
                    
        elif opcion =="2":
            
        elif opcion == 3:
            gestor_de_gastos()
            
        elif opcion == 4:
         
        elif opcion =="5":
            print("Saliendo del programa, gracias :) ")
            break
        else:
            print("opcion no válida. Intentalo de nuevo.")
main()





 
