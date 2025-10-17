Mi parte del proyecto respecto a las finanzas personales va a ser el simulador e deudas y coimo van cambiando las cuotas segun los plazos y los interes, y lo vamos a hacer de tal manera para que los usuarios puedan ver y entender cómo cambian sus pagos dependiendo de cuánto pide prestado, la tasa de interés y el tiempo que elige para pagar. 

La idea del programa es que el ususario pueda escribir la cantidad de su deuda, su interes, y el plazo en meses y en base a esta informacion, el programa le va a muestrar cuánto tendría que pagar en cada cuota ya se mensual o quincenal. Lo que va a hacer interesante es que el usuario va a poder entender que si quiere pagar una x cantidad a mas meses, pues al final va a pagar mas porque los intereses van a subir pero si realiza un plazo de menos meses, al final va a pagar una manor cuota. 

Una vez que el usuario vea los diferentes plazos y las diferentes cuotas en base a lo que acabo de explicar, el usuario va a comparar distintos escenarios y diferentes cuotas y va a analizar cual opcion es la mas conveniente para el, y esto es muy importante en la vida financiera porque va a empezar a tomar buenas decisiones en base al dinero y a futuro, le va a ayudar mucho en su vida financiera.




                                                   Algoritmo

1. Solicitar al usuario:
  1.1:El monto total de la deuda
  1.2:El interés anual
  1.3:El número de meses para pagar

2. Llamar a la función calcular_cuota_mensual(monto, interes_anual, meses) - (datos que recibe)
   2.1:Esta funcion calcula  interes mensual , diviendo  tasa anual entre 12
   2.2:Si el interes es 0, la deuda se divide entre los meses para asi obtener pagos iguales
   2.3:Si hay interes, se usa la formula y asi se asegura que cada vez sea el mismo agp mensual
   2.4:Si los valores son invalidos, ya sean montos negativos o interes negativo, regresa por medio de un str un mensaje de error
   2.5:Regresa los valores de la cuota mensual - (datos que regresa)
    
3. Llamar a la funcion alcular_cuota_quincenal(monto, interes_anual, meses) - (datos que recibe)
   3.1:Esta funcion lo que hace es convertir los meses en quincenas multiplicano por 2
   3.2:Calcula el interes quincenal diviendo el interes_anual entre 24
   3.3:Si los valores son invalidos, ya sean montos negativos o interes negativo, regresa por medio de un str un mensaje de error
   3.4:Regresa los valores de la cuota quincenal - (datos que regresa)

4. Llamar a la función calcular_interes_total_mensual(monto, interes, meses) - (datos que recibe)
   4.1: Calcula la cuota mensual con la funcion calcular_cuota_mensual()
   4.2: MUltiplica la cuota mensual por la cantidad de meses
   4.3: Resta el monto original al total pagado para obtener el interés total.
   4.4: Regresa el valor del interes total mensual - (datos que regresa)

5. Llamar a la funcion calcular_interes_total_quincenal(monto, interes, meses) - (datos que recibe)
   5.1: Calcula la cuota quincenal con la función calcular_cuota_quincenal()
   5.2: Multiplica la cuota quincenal por el número total de quincenas
   5.3: Resta el monto original al total pagado para obtener el interés total
   5.4: Regresa el valor el interes total quincenal - (datos que regresa)
   
6. Llamar a la función calcular_escenarios(monto, interes, meses) - (datos que recibe)
   6.1:Esta función crea diferentes escenarios para cada plazo ya sea de 1 mes o hasta n cantidad
   6.2:Calcula tanto la cuota mensual como la quincenal para ese plazo
   6.3:Guarda los resultados en una matriz
   6.4:Regresa la matriz - (datos que regresa)
   
7. Llamar a la función calcular_total_pagar(monto, interes, meses) - (datos que recibe)
   7.1:Calcula los totales de pago tanto mensuales como quincenales llamando a sus respectivas funciones
   7.2:Multiplica la cuota por el numero de meses que son
   7.3:Una lista va guardando los resultados
   7.4:Regresa la lista los totales a pagar - (datos que regresa)

8. Llamar a la funcion guardar_escenarios(monto, interes, meses)
   8.1:Usa los resultados de la funcion calcular_escenarios() - (datos que usa)
   8.2:Crea un archivo llamado escenarios_deuda.csv 
   8.3:Guarda en el archivo las columnas: Plazo, Cuota Quincenal y Cuota Mensual
   8.4:Regresa un mensaje confirmando que todos los archivos se guardaron correctamente - (datos que regresa)

9. Llamar a la función guardar_totales(monto, interes, meses
   9.1:Usa los resultados de calcular_total_pagar() - (datos que usa)
   9.2:Crea un archivo llamado totales_deuda.csv
   9.3:Guarda en el archivo las columnas: Plazo, Total Quincenal y Total Mensual
   9.4:Regresa un mensaje confirmando que los escenarios se guardaron correctamente - (datos que regresa)
   
10. Llamar a la función pruebas()
   10.1:Realiza diferentes pruebas automáticas para corroborar que el codgio funciona correctamente
   10.2:Comprueba los resultados con assert para detectar errores
   10.3:Si todas las pruebas pasan, regresa un mensaje indicando que todo está correcto - (datos que regresa)
   10.4:Si las pruebas no pasan, regresa un mensaje indicando que el codigo esta mal - (datos que regresa)

11. Llamar a la función pedir_datos() 
   11.1:Solicita al usuario los valores necesarios (monto, interés y meses) - (datos que recibe)
   11.2:Regresa los valores para usarlos en las funciones necesaarias - (datos que regresa)
    
12.Funcion main()
   12.1:El programa le pide los datos al usuario
   12.2:El usuario puede elegir que ver entre el pago mensual, quincenal, escenarios o totales
   12.3:Muestra los resultados en pantalla y los guarda en archivos si es necesario

13. El usuario decide si continuar o no



El objetivo del algoritmo es simular el comportamiento de una deuda dependiendo del monto, la tasa de interés y el plazo en meses que el 
usuario tenga. Permite conocer cuánto tendría que pagar si realiza pagos mensuales o quincenales, mostrando una tabla con los distintos 
escenarios. Cada función del programa se encarga de un cálculo específico: una calcula la cuota mensual, otra la quincenal, otra genera los 
escenarios y otra suma el total a pagar. Esto facilita ver de una manera sencilla cómo varían los pagos según el plazo y la tasa de interés. De 
esta manera, el usuario puede planificar sus pagos y entender el impacto del interés en la deuda total, ya que si suben los meses, sube el 
interes, y si sube el interes, sube el costo total a pagar.








                                                   Algoritmo del mian()


1. El ususario escoge la opcion 4 == Simulador de Deuda
   1.1 La funcion llama a la funcion pedir_datos() 

2. Se muestra el MENU de todas las opciones

3. Si opcion == 1 - Llama a calcular_cuota_mensual(monto, interes, meses)
   3.1:Imprime el pago mensual

4. Si opcion == 2 - Llama a calcular_cuota_quincenal(monto, interes, meses)
   4.1:Imprime el pago quincenal
   
5. Si opcion == 3 - Llama a calcular_escenarios(monto, interes, meses)
   5.1:Imprime las filas con columnas mostrando los diferentes escenarios

6. Si opcion == 4 - Llama a calcular_total_pagar(monto, interes, meses)
   6.1:Imprime una tabla con los totales acumulados para cada mes

7. Si opcion == 5 - Llama a calcular_interes_total_mensual(monto, interes, meses)
   7.1:Imprime el interes total mensual que el usuaio va a pagar 

8. Si opcion == 6 - Llama a calcular_interes_total_quincenal(monto, interes, meses)
   8.1:Imprime el interes total quincenal que el usuaio va a pagar

9. Si opcion == 7 - Llama a guardar_escenarios(monto, interes, meses)
   9.1:Crea un archivo escenarios_deuda.csv
   9.2:Imprime el mensaje de confirmacion

10. Si opcion == 8 - Llama a guardar_totales(monto, interes, meses)
   10.1:Llama a guardar_totales(monto, interes, meses)
   10.2:Crea un archivo totales_deuda.csv
   10.3:Imprime el mensaje de confirmacion

11. Si opcion == 9 - Llama a pruebas()
   11.1:Imprime que las pruebas pasaron correctamente

12. Si opcion == 10 - Se termina el ciclo

13. Si el usuario ingresa un numero invalido
   13.1:Imprime "Selecciona una opción válida"









     
   

                                                   
