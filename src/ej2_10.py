def elegir_tipo(tipo=0):
    print("Elije el tipo de pizza: ")
    print("1. Pizza vegetariana")
    print("2. Pizza no vegetariana")
    tipo = int(input())
    if tipo > 0 and tipo <= 2:
        return tipo
    else:
        return None

def elegir_ingredientes(tipo, ingredientes=["Tomate", "Mozzarella"]):
    if tipo == None:
        return None
    print("Ingredientes disponibles: ")
    if tipo == 1:
        print("1. Pimiento")
        print("2. Tofu")
        ingrediente_a_elegir = int(input())
        if ingrediente_a_elegir == 1:
            ingredientes.append("Pimiento")
        elif ingrediente_a_elegir == 2:
            ingredientes.append("Tofu")
    else:
        print("1. Peperoni")
        print("2. Jamón")
        print("3. Salmon")
        ingrediente_a_elegir = int(input())
        if ingrediente_a_elegir == 1:
            ingredientes.append("Pepperoni")
        elif ingrediente_a_elegir == 2:
            ingredientes.append("Jamón")
        elif ingrediente_a_elegir == 3:
            ingredientes.append("Salmon")


    if len(ingredientes) == 2:
        return None
    
    return ingredientes

def formar_eleccion(tipo, ingredientes):
    if tipo == None:
        return "No has ingresado un ingrediente o un tipo de pizza válido"
    if not ingredientes or len(ingredientes) <= 2:
        return "No tienes suficentes ingredientes o no lo has elegido bien"
    if tipo == 1:
        resultado = "Has elegido una pizza vegetariana con los siguientes ingredientes: "
    if tipo == 2:
        resultado = "Has elegido una pizza NO vegetariana con los siguientes ingredientes: "
    resultado += ", ".join(ingredientes)
    return resultado
        
def main():
    tipo = elegir_tipo()
    ingredientes = elegir_ingredientes(tipo)
    print(formar_eleccion(tipo, ingredientes))

if __name__ == "__main__":
    main()