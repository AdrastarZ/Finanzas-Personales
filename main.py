from GestorGastos.Gestor_de_gastos import gestor_de_gastos

def menu():
    print("\n--- Menú Principal ---")
    print("3.Gestor de gastos")
    print("5.Salir")


def main ():
  while True:
    menu()
    opcion=int(input("Ingresa una opcion: "))

    elif opcion == 3:
      gestor_de_gastos()
    elif opcion ==5:
      break
    else:
      print("Ingresa una opcion valida")

main()

