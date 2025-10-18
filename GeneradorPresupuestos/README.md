AdrastarZ

Un generador de presupuestos es una herramienta que permite calcular, organizar y presentar estimaciones de costos de manera rápida y precisa. Su función principal es ahorrar tiempo, reducir errores y facilitar la gestión de recursos en diferentes tipos de proyectos.

Su importancia radica en que automatiza operaciones que de forma manual serían tardadas y propensas a equivocaciones, al mismo tiempo que aporta claridad y transparencia en la presentación de los costos. Esto ayuda a mejorar la toma de decisiones y permite comparar diferentes escenarios financieros de forma sencilla.

Entre sus aplicaciones se encuentran la elaboración de cotizaciones para empresas y freelancers, la planeación de proyectos en áreas como construcción, diseño o desarrollo de software, así como la administración de gastos personales o familiares. También es útil para pequeños negocios que requieren generar presupuestos sin necesidad de sistemas contables complejos.

Funcionalidades:
1. Definir a detalle las areas de gasto y su cantidad
2. El porcentaje que se gasta y comparacion con el capital inicial
3. Descubrir si hay capital sobrante despues del presupuesto establecido

Algoritmo:

1. función crea_lista:

Entrada:
Vacio

Proceso:
1. Mientras el ciclo sea verdadero:

   1.1 Solicita un valor al usuario
   
   1.2 Si el valor en minúsculas es igual a "fin" y la longitud de la lista es mayor a 0:

   1.2.1 Rompe el ciclo

   1.3 Si no, Si el valor en minúsculas es igual a "fin" y la longitud de la lista es menor a 1:

   1.3.1 Imprimir mensaje 1

   1.4 Si no, Si el valor tiene dígitos:

   1.4.1 Imprimir mensaje 2

   1.5 Si no

   1.5.1 Añade valor insertado por el usuario a la lista, lo pone en minúsculas y lo capitaliza
2. Devuelve lista

Salida:
Mensaje 1 o mensaje 2 o lista devuelta


2. función futuro_gasto:

Entrada:
Lista de sectores

Proceso:
1. Para i en rango de la longitud de la lista:

   1.1 Mientras que el ciclo se verdadero:

   1.1.1 Intenta:
   
   1.1.1.1 Solicitar al usuario el valor de costo

   1.1.2 En caso de que la solicitud tenga un error:

   1.1.2.1 Imprimir mensaje

   1.1.3 Si no:

   1.1.3.1 Rompe el ciclo

   1.2 Añadir a mi lista de costo por sector el valor de costo

Salida:
Lista de costo por sector devuelta


3. función sector_costo:

Entrada: 
lista de sectores y lista de costos

Proceso:
1. Para i en un rango de un tamaño de mi lista de sectores:
   
   1.1 Un mensaje se guarda con los datos de lista y de costo
   
   1.2 El mensaje se añade a la lista de mensajes

2. Devolver lista de mensajes

Salida:
Lista de mensajes


4. función porcentajes:

Entrada:
Lista de sectores y lista de costo

Proceso:
1. Para s en un rango de la longitud de mi lista de costo

   1.1 Mi suma se le añade el valor de mi lista de costo en la posición s

2. Para i en un rango de longitud de mi lista de costo

   2.1 Mi porcentaje es igual a la lista de costo en la posición i sobre la suma, multiplicado por 100

   2.2 Un mensaje se guarda con los datos de lista y de porcentaje

   2.3 El mensaje se añade a la lista de mensajes

   2.4 El porcentaje se añade a la lista de porcentajes

3. Devuelve la lista de mensajes y la lista de porcentajes

Salida:
Lista de porcentajes y lista de mensajes


5. función sobrante:

Entrada:
Valor de ganancias y lista de costo

1. Para s en un rango de la longitud de mi lista de costo

   1.1 Mi suma se le añade el valor de mi lista de costo en la posición s

2. Residuo es igual a las ganancias menos el valor de suma

3. Si mis ganancias son mayores a mi suma

   3.1 El mensaje se guarda diciendo que hay dinero sobrante

4. Si no, Si mis ganancias son iguales a mi suma

   4.1 El mensaje se guarda diciendo que el dinero es justo

5. Si no, Si mis ganancias son menores a mi suma

   5.1 El mensaje se guarda diciendo que no hay dinero suficiente

6. Devuelve el mensaje y el valor del residuo

Salida:
Mensaje y valor de residuo devueltos


6. función guardaRegistro:

Entrada:
Lista de sectores, lista de costos, lista de porcentajes y valor sobrante

Proceso:
1. La variable registro es igual a la localización del documento Registro.txt en el proyecto

2. Si el porcentaje es None:

   2.1 Para i en un rango de la longitud de mi lista de sectores

   2.1.1 Añadir "N/A" al final de la lista

3. Si el sobrante es None:

   3.1 El valor de sobrante es un mensaje

4. Abrir el archivo Registro en modo append

5. Escribir en columnas imaginarias "Sector" con separación de 15, "Costo" con separación de 10 y "Porcentaje" con separación de 15

6. Para i en un rango de la longitud de mi lista

   6.1 Si el estado de porcentajes en la posición i es un int o float

   6.1.1 Escribe el valor de lista de sectores en la posición i con separación de 15, el valor de lista de costo en la posición i con separación de 5 y el valor de lista de porcentaje en la posición i con separación de 15 y 2 decimales

   6.2 Si no

   6.2.1 Escribe el valor de lista de sectores en la posición i con separación de 15, el valor de lista de costo en la posición i con separación de 5 y el valor de lista de porcentaje en la posición i con separación de 15

7. Cierra el archivo

Salida
Archivo Registro.txt con datos nuevos añadidos


7. función borra Registro

Entrada:
Valor "seguro"

Proceso:
1. La variable registro es igual a la localización del documento Registro.txt en el proyecto

2. Mientras que el ciclo sea verdadero

   2.1 Si mi valor "seguro" en minúsculas es igual a "y":

   2.1.1 Abrir el archivo Registro en modo write

   2.1.2 Escribir un nada

   2.1.3 Cerrar archivo Registro

   2.1.4 Romper ciclo

   2.2 Si no, Si mi valor "seguro" en minúsculas es igual a "n":

   2.1.1 Imprimir mensaje 1

   2.2.2 Romper ciclo

   2.3 Si no

   2.3.1 Imprimir mensaje 2

   2.3.2 Romper ciclo

Salida:
Archivo Registro.txt sobrescrito o mensaje 1 impreso o mensaje 2 impreso
   

   



        
