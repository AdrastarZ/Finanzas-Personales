Mi parte del proyecto respecto a las finanzas personales va a ser el simulador e deudas y coimo van cambiando las cuotas segun los plazos y los interes, y lo vamos a hacer de tal manera para que los usuarios puedan ver y entender cómo cambian sus pagos dependiendo de cuánto pide prestado, la tasa de interés y el tiempo que elige para pagar. 

La idea del programa es que el ususario pueda escribir la cantidad de su deuda, su interes, y el plazo en meses y en base a esta informacion, el programa le va a muestrar cuánto tendría que pagar en cada cuota ya se mensual o quincenal. Lo que va a hacer interesante es que el usuario va a poder entender que si quiere pagar una x cantidad a mas meses, pues al final va a pagar mas porque los intereses van a subir pero si realiza un plazo de menos meses, al final va a pagar una manor cuota. 

Una vez que el usuario vea los diferentes plazos y las diferentes cuotas en base a lo que acabo de explicar, el usuario va a comparar distintos escenarios y diferentes cuotas y va a analizar cual opcion es la mas conveniente para el, y esto es muy importante en la vida financiera porque va a empezar a tomar buenas decisiones en base al dinero y a futuro, le va a ayudar mucho en su vida financiera.




                                                   Algoritmo

1. Solicitar al usuario:
  1.1:El monto total de la deuda
  1.2:El interés anual
  1.3:El número de meses para pagar

2. Llamar a la función calcular_cuota_mensual(monto, interes_anual, meses)
   2.1:Esta funcion calcula  interes mensual , diviendo  tasa anual entre 12
   2.2:Si el interes es 0, la deuda se divide entre los meses para asi obtener pagos iguales
   2.3:Si hay interes, se usa la formula y asi se asegura que cada vez sea el mismo agp mensual
   2.4:Si los valores son invalidos, ya sean montos negativos o interes negativo, regresa por medio de un str un mensaje de error
   2.5:Regresa los valores de la cuota mensual
    
3. Llamar a la funcion alcular_cuota_quincenal(monto, interes_anual, meses)
   3.1:Esta funcion lo que hace es convertir los meses en quincenas multiplicano por 2
   3.2:Calcula el interes quincenal diviendo el interes_anual entre 24
   3.3:Si los valores son invalidos, ya sean montos negativos o interes negativo, regresa por medio de un str un mensaje de error
   3.4:Regresa los valores de la cuota quincenal
   
4. Llamar a la función calcular_escenarios(monto, interes, meses)
   4.1:Esta función crea diferentes escenarios para cada plazo ya sea de 1 mes o hasta n cantidad
   4.2:Calcula tanto la cuota mensual como la quincenal para ese plazo
   4.3:Guarda los resultados en una matriz
   4.4:Devuelve la matriz

5. Llamar a la función calcular_total_pagar(monto, interes, meses)
   5.1:Usa la matriz de devuelve la funcion calcular_escenarios(monto, interes, meses)
   5.2:Suma cada una de las cuotas mensuales para obtener total a pagar al final del periodo
   5.3:Devuelve  cantidad que el usuario va a pagar en total

6. Llamar a la funcion main()
   6.1:Se muestran los mensajes de que es lo que el usuario quiere ver si el costo mensual, quincenal o el escenario
   6.2:Se imprime la tabla e¿ordenada con los datos que el usuario desee
   6.3:Imprime  total a pagar
   
7. El usuario decide si continuar o no



El objetivo del algoritmo es simular el comportamiento de una deuda dependiendo del monto, la tasa de interés y el plazo en meses que el usuario tenga. Permite conocer cuánto tendría que pagar si realiza pagos mensuales o quincenales, mostrando una tabla con los distintos escenarios. Cada función del programa se encarga de un cálculo específico: una calcula la cuota mensual, otra la quincenal, otra genera los escenarios y otra suma el total a pagar. Esto facilita ver de una manera sencilla cómo varían los pagos según el plazo y la tasa de interés. De esta manera, el usuario puede planificar sus pagos y entender el impacto del interés en la deuda total, ya que si suben los meses, sube el interes, y si sube el interes, sube el costo total a pagar.











     
   

                                                   
