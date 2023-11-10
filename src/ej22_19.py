def menu():
    while True:
        print("Menú:")
        print("1 - Comenzar programa")
        print("2 - Imprimir listado")
        print("3 - Finalizar programa")
        opcion = input("Selecciona una opción (1/2/3): ")
        if opcion == "1":
            print("Iniciando programa")
        elif opcion == "2":
            print("Imprimiendo listado")
        elif opcion == "3":
            print("Finalizando programa.")
            break
        else:
            print("Opción incorrecta")

def main():
    menu()

if __name__ == "__main__":
    main()