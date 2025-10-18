# Finanzas-Personales
Las finanzas es una herramienta sumamente importante en la actualidad. La importacia radica en la capacidad de crecimiento economico tanto para grandes cuerpos como para individuos, permitiendo la toma de decisiones informadas sobre cómo obtener, administrar y usar los recursos monetarios. Su función es clave para la planificación de metas a largo plazo, la gestión de riesgos, el cumplimiento de obligaciones y la maximización del valor, asegurando la viabilidad económica y la prosperidad en diversos escenarios

En este repositorio se encontraran 4 diferentes proyectos con el objetivo del dessarrollo de multiples herramientas financieras.

1. Calculadora de intéres compuesto.
2. Generador de presupuesto
3. Gestor de gastos.
  
4. Simulador de deudas.

Algoritmo del main(). Calculadora de interés compuesto

- Entradas:No recibe parámetros directamente el main conrrespecto a la Calculadora de interés compuesto, pero el usuario ingresa información mediante un input en cada menú individual de cada archivo.
  
- procesos:
1. Se inicia con una variable activo = True para mantener el programa funcionando mientras el usuario no elija “Salir"
2. El usuario selecciona == "1":
3. Usa otro while True que controla las operaciones de la calculadora (préstamos, inversiones, historial).
4. El main lo reedirecciona a el menu de la carpeta de CalculadoraInteresCompuesto.
5. El usuario selecciona alguna de las 4 opciones que le son proporcionadas por el menú del archivo de interes_compuesto.
6. En el momento que seleccione una operación todo quedara registrado en las listas: Historial_prestamos = [], realizadoshistorial_inversiones = [] para al final obtener todos los resultados que el usuario seleccionó, usando diccionarios para almacenar la información.
7. Si se selecciona “Salir”, cambia activo = False y rompe el ciclo principal.
   
- Salidas:
1. Despliega resultados, menús, y tablas en pantalla.
2. Retiene los datos procesados dentro de los historiales.
3. Finaliza el programa cuando el usuario selecciona la opción 5.





Algoritmo del main() - Generador de presupuesto

1. Valor de lista es igual a la funcion crea_lista llamada desde Generador de Presupuestos
2. Valor de costo es igual a la función futuro_gasto llamada desde Generador de Presupuestos
3. Mientras que el ciclo sea verdadero
   
   3.1 Llama a la función menu llamada desde Generador de Presupuestos
   
   3.2 Solicita al usuario que escoja una opción para el generador de presupuestos

   3.3 Si la opción del generador de presupuestos es igual a 1

   3.3.1 Para m en la función sector_costo llamada desde Generador de Presupuestos

   3.3.1.1 Imprime "m"

   3.4 Si no, Si la opción del generador de presupuestos es igual a 2

   3.4.1 mensajePor y porcentaje son iguales a la función porcentajes llamada desde Generador de Presupuestos

   3.4.2 Para m en mensajePor

   3.4.2.1 Imprime "m"

   3.5 Si no, Si la opción del generador de presupuestos es igual a 3

   3.5.1 Se le solicita el valor ganancias al usuario

   3.5.2 mensajeSob y sobrante son iguales a la función sobrante llamada desde Generador de Presupuestos

   3.5.3 Imprimir mensajeSob

   3.6 Si no, Si la opción del generador de presupuestos es igual a 4

   3.6.1 Usa la función guardaRegistro llamada desde Generador de Presupuestos

   3.7 Si no, Si la opción del generador de presupuestos es igual a 5

   3.7.1 Solicita al usuario el valor seguro

   3.7.1 Usa la función borraRegistro llamada desde Generador de Presupuestos

   3.8 Si no, Si la opción del generador de presupuestos es igual a 6

   3.8.1 Mientras que el ciclo sea verdadero

   3.8.1.1 Solicita al usuario el valor nuevaVieja

   3.8.1.2 Si el valor nuevaVieja en minúsculas es igual a "y"

   3.8.1.2.1 Valor "sobrante" es igual a None

   3.8.1.2.2 Valor "porcentaje" es igual a None

   3.8.1.2.3 Valor de lista es igual a la función crea_lista llamada desde Generador de Presupuestos

   3.8.1.2.4 Valor de costo es igual a la función futuro_gasto llamada desde Generador de Presupuestos

   3.8.1.2.5 Rompe el ciclo

   3.8.1.3 Si no, Si el valor nuevaVieja en minúsculas es igual a "n"

   3.8.1.3.1 Rompe el ciclo

   3.8.1.4 Si no

   3.8.1.4.1 Imprime mensaje

   3.9 Si no, Si la opción del generador de presupuestos es igual a 7

   3.9.1 Usa la función casos_prueba llamada desde Generador de Presupuestos

   3.10 Si no, Si la opción del generador de presupuestos es igual a 8

   3.10.1 Imprime Mensaje

   3.10.2 Rompe el ciclo

   3.11 Si no

   3.11.1 Imprime mensaje


Algoritmo del main() - Simulador de Deuda

1. El usuario escoge la opción 4 == Simulador de Deuda
   1.1 La funcion llama a la funcion pedir_datos() 


2. Se muestra el MENÚ de todas las opciones


3. Si opción == 1 - Llama a calcular_cuota_mensual(monto, interes, meses)
   3.1:Imprime el pago mensual


4. Si opcion == 2 - Llama a calcular_cuota_quincenal(monto, interes, meses)
   4.1:Imprime el pago quincenal
   
5. Si opcion == 3 - Llama a calcular_escenarios(monto, interes, meses)
   5.1:Imprime las filas con columnas mostrando los diferentes escenarios


6. Si opción == 4 - Llama a calcular_total_pagar(monto, interes, meses)
   6.1:Imprime una tabla con los totales acumulados para cada mes


7. Si opcion == 5 - Llama a calcular_interes_total_mensual(monto, interes, meses)
   7.1:Imprime el interés total mensual que el usuario va a pagar 


8. Si opcion == 6 - Llama a calcular_interes_total_quincenal(monto, interes, meses)
   8.1:Imprime el interés total quincenal que el usuario va a pagar


9. Si opción == 7 - Llama a guardar_escenarios(monto, interes, meses)
   9.1:Crea un archivo escenarios_deuda.csv
   9.2:Imprime el mensaje de confirmación


10. Si opción == 8 - Llama a guardar_totales(monto, interes, meses)
   10.1:Llama a guardar_totales(monto, interes, meses)
   10.2:Crea un archivo totales_deuda.csv
   10.3:Imprime el mensaje de confirmación


11. Si opción == 9 - Llama a pruebas()
   11.1:Imprime que las pruebas pasaron correctamente


12. Si opción == 10 - Se termina el ciclo


13. Si el usuario ingresa un numero invalido
   13.1:Imprime "Selecciona una opción válida"





   
4. Generador de presupuestos.
