import datetime

# -------------------- Variables globales --------------------
movimientos = []         # Lista de movimientos (ingresos/egresos)
presupuesto_mensual = 0  # Límite de egresos por mes
meta_ahorro = 0          # Meta de ahorro deseada


# -------------------- Funciones principales --------------------
def registrar_movimiento(tipo, monto=None, categoria=None, fecha=None):
    """
    Registra un ingreso o egreso.
    Parámetros opcionales para facilitar pruebas.
    Devuelve True si se registró con éxito, False si hubo error.
    """
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
        return True
    except ValueError:
        print("Monto inválido.")
        return False


def calcular_totales():
    """
    Calcula totales de ingresos, egresos y balance.
    Devuelve (ingresos, egresos, balance).
    """
    ingresos = sum(m["monto"] for m in movimientos if m["tipo"] == "ingreso")
    egresos = sum(m["monto"] for m in movimientos if m["tipo"] == "egreso")
    return ingresos, egresos, ingresos - egresos


def mostrar_resumen():
    """
    Muestra:
      - Totales de ingresos, egresos y balance
      - Lista detallada de movimientos (usa for)
      - Alertas según presupuesto o meta de ahorro
    """
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

    # ----- Estructuras de decisión para alertas -----
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


def establecer_presupuesto(valor=None):
    """
    Define el presupuesto mensual máximo de egresos.
    """
    global presupuesto_mensual
    try:
        if valor is None:
            valor = float(input("Presupuesto mensual: "))
        presupuesto_mensual = float(valor)
        return True
    except ValueError:
        print("Valor inválido.")
        return False


def establecer_meta(valor=None):
    """
    Define la meta de ahorro.
    """
    global meta_ahorro
    try:
        if valor is None:
            valor = float(input("Meta de ahorro: "))
        meta_ahorro = float(valor)
        return True
    except ValueError:
        print("Valor inválido.")
        return False


# -------------------- Pruebas automáticas --------------------
def caso_prueba_demo():
    """
    Caso de prueba que registra varios movimientos, establece presupuesto y meta,
    y muestra resultados automáticamente.
    """
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


# Para ejecutar este caso de prueba, solo llama:
caso_prueba_demo()


# -------------------- Menú interactivo --------------------
def menu():
    """
    Muestra el menú y devuelve la opción elegida.
    """
    print("\n--- GESTOR DE GASTOS ---")
    print("1. Registrar ingreso")
    print("2. Registrar egreso")
    print("3. Ver resumen")
    print("4. Establecer presupuesto mensual")
    print("5. Establecer meta de ahorro")
    print("6. Ejecutar pruebas")
    print("7. Salir")
    return input("Elige una opción: ")


def gestor_de_gastos():
    """
    Bucle principal del programa (while infinito hasta salir).
    Usa estructuras de decisión para llamar a cada función según la opción.
    """
    while True:  # comportamiento cíclico
        opcion = menu()
        if opcion == "1":
            registrar_movimiento("ingreso")
        elif opcion == "2":
            registrar_movimiento("egreso")
        elif opcion == "3":
            mostrar_resumen()
        elif opcion == "4":
            establecer_presupuesto()
        elif opcion == "5":
            establecer_meta()
        elif opcion == "6":
            caso_prueba_demo()
        elif opcion == "7":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")


if __name__ == "__main__":
    gestor_de_gastos()



