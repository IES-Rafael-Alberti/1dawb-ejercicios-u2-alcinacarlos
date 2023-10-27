def elegir_pizza():
    opcion = input("Elija 1 o 2: ")
    ingredientes = []
    tipo_pizza = None
        
    if opcion == "1":
        tipo_pizza = "vegetariana"
        print("Ingredientes disponibles: ")
        print("1. Pimiento")
        print("2. Tofu")
        seleccion = input("Elije un ingrediente: ")
        
        if seleccion == "1":
            ingredientes.append("Pimiento")
        elif seleccion == "2":
            ingredientes.append("Tofu")
        else:
            print("Selección no válida.")

    elif opcion == "2":
        tipo_pizza = "no vegetariana"
        print("Ingredientes disponibles: ")
        print("1. Peperoni")
        print("2. Jamón")
        print("3. Salmón")
        seleccion = input("Elije un ingrediente: ")    
        if seleccion == "1":
            ingredientes.append("Peperoni")
        elif seleccion == "2":
            ingredientes.append("Jamón")
        elif seleccion == "3":
            ingredientes.append("Salmón")
        else:
            print("Selección no válida.")

    if tipo_pizza != None and ingredientes:
        print("Pizza", tipo_pizza, "con los siguientes ingredientes:")
        ingredientes.append("Mozzarella")
        ingredientes.append("Tomate")
        for i in ingredientes:
            print(i)
    else:
        print("No has introducido bien los valores.")
        
    
def main():
    print("1. Pizza vegetariana")
    print("2. Pizza no vegetariana")
    elegir_pizza()


if __name__ == "__main__":
    main()