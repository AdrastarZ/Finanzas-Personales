import datetime
import json

# Variables globales 
movimientos = []         # Lista de movimientos (ingresos/egresos)
presupuesto_mensual = 0  # Límite de egresos por mes
meta_ahorro = 0          # Meta de ahorro deseada
archivo_json = "movimientos.json"
# Funciones JSON

 #Esta funcion se encarga de guardar los movimientos realizados dentro de un archivo
def guardar_json(): 
    global movimientos
    try:
        with open(archivo_json, "w") as f:
            json.dump(movimientos, f, default=str, indent=4)
        return True
    except Exception as e:
        print(f"Error al guardar: {e}")
        return False

#Se encarga de leer la informacion dentro del archivo y la sube a las variables globales
def cargar_json():
    
    global movimientos
    try:
        with open(archivo_json, "r") as f:
            movimientos_cargados = json.load(f)
            for m in movimientos_cargados:
                if isinstance(m["fecha"], str):
                    m["fecha"] = datetime.datetime.strptime(m["fecha"], "%Y-%m-%d").date()
            movimientos = movimientos_cargados
        print("Movimientos cargados correctamente.")
        return True
    except FileNotFoundError:
        print("Archivo no encontrado, se creará uno nuevo al guardar.")
        return False
    except Exception as e:
        print(f"Error al cargar: {e}")
        return False


# Funciones principales

 
# Registra un ingreso o egreso.
# Parámetros para facilitar pruebas.
# Devuelve True si se registró con éxito, False si hubo error.
def registrar_movimiento(tipo,monto=None,categoria=None,fecha=None):
    
    global movimientos
    try:
        if monto is None:
            monto = float(input("Monto: "))
        if categoria is None:
            categoria = input("Categoría (comida, transporte, etc.): ")
        if fecha is None:
            fecha = datetime.date.today()
        movimientos.append({
            "tipo": tipo,
            "monto": float(monto),
            "categoria": categoria,
            "fecha": fecha
        })
        guardar_json()  
        return True
    except ValueError:
        print("Monto inválido.")
        return False

# Calcula totales de ingresos, egresos y balance.
# Devuelve (ingresos, egresos, balance).
def calcular_totales():
    ingresos = sum(m["monto"] for m in movimientos if m["tipo"] == "ingreso")
    egresos = sum(m["monto"] for m in movimientos if m["tipo"] == "egreso")
    return ingresos, egresos, ingresos - egresos


# Totales de ingresos, egresos y balance
#Muestra
# Lista detallada de movimientos (usa for)
# Alertas según presupuesto o meta de ahorro
def mostrar_resumen():
   
    ingresos, egresos, balance = calcular_totales()
    print("\n--- RESUMEN ---")
    print(f"Ingresos: ${ingresos:.2f}")
    print(f"Egresos:  ${egresos:.2f}")
    print(f"Balance:  ${balance:.2f}")

    # Ciclo for para mostrar cada movimiento
    if not movimientos:
        print("No hay movimientos registrados.")
    else:
        for idx, mov in enumerate(movimientos, start=1):
            print(f"{idx}. {mov['fecha']} - {mov['tipo'].capitalize()}: "
                  f"${mov['monto']:.2f} ({mov['categoria']})")

    # Estructuras de decisión para alertas
    if presupuesto_mensual > 0:
        if egresos > presupuesto_mensual:
            print("Presupuesto mensual superado.")
        elif egresos > 0.9 * presupuesto_mensual:
            print("Estás por alcanzar tu presupuesto.")

    if meta_ahorro > 0:
        if balance >= meta_ahorro:
            print("¡Meta de ahorro alcanzada!")
        else:
            print(f"Meta de ahorro (${meta_ahorro:.2f}) aún no alcanzada.")

 
#Define el presupuesto mensual máximo de egresos.
def establecer_presupuesto(valor=None):
    
    global presupuesto_mensual
    try:
        if valor is None:
            valor = float(input("Presupuesto mensual: "))
        presupuesto_mensual = float(valor)
        return True
    except ValueError:
        print("Valor inválido.")
        return False

#Esta duncion se encarga de definir la meta de ahorro.
def establecer_meta(valor=None):
   
    global meta_ahorro
    try:
        if valor is None:
            valor = float(input("Meta de ahorro: "))
        meta_ahorro = float(valor)
        return True
    except ValueError:
        print("Valor inválido.")
        return False


# Pruebas automáticas
#Caso de prueba que registra varios movimientos, establece presupuesto, meta y muestra resultados automáticamente.
def caso_prueba_demo():
  
    global movimientos, presupuesto_mensual, meta_ahorro

    print("\n=== INICIANDO CASO DE PRUEBA DEMO ===")

    # Reiniciar datos
    movimientos = []
    presupuesto_mensual = 0
    meta_ahorro = 0

    # 1️ Registrar movimientos
    registrar_movimiento("ingreso", 2000, "sueldo", datetime.date(2025, 9, 1))
    registrar_movimiento("egreso", 500, "renta", datetime.date(2025, 9, 2))
    registrar_movimiento("egreso", 150, "comida", datetime.date(2025, 9, 3))
    registrar_movimiento("ingreso", 300, "freelance", datetime.date(2025, 9, 4))
    registrar_movimiento("egreso", 100, "transporte", datetime.date(2025, 9, 5))

    # 2️ Establecer presupuesto y meta de ahorro
    establecer_presupuesto(700)
    establecer_meta(1000)

    # 3️ Mostrar resumen
    mostrar_resumen()

    # 4️ Validar resultados automáticamente
    ingresos, egresos, balance = calcular_totales()
    print("\n--- RESULTADOS DE LA PRUEBA ---")
    print(f"Total ingresos esperados: 2300, calculados: {ingresos}")
    print(f"Total egresos esperados: 750, calculados: {egresos}")
    print(f"Balance esperado: 1550, calculado: {balance}")
    print("=== FIN DEL CASO DE PRUEBA ===\n")

# Menú interactivo
# Muestra el menú y devuelve la opción elegida.
def menu():

    print("\n--- GESTOR DE GASTOS ---")
    print("1. Registrar ingreso")
    print("2. Registrar egreso")
    print("3. Ver resumen")
    print("4. Establecer presupuesto mensual")
    print("5. Establecer meta de ahorro")
    print("6. Ejecutar pruebas")
    print("7. Salir")
    return input("Elige una opción: ")













