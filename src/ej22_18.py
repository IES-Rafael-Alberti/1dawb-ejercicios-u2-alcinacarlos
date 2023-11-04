def menu():
    contador = 0
    resultado = 0
    numero = input()
    if numero.strip("-").isdigit() == False:
        return "Numero ingresado no válido, tiene que ser positivo"
    else:
        numeroint = int(numero)
    while numeroint != -1:
        while contador != len(numero):
            resultado += int(numero[contador])
            contador += 1
        print(resultado)
        resultado = 0
        contador = 0
        numero = input()
        if numero.strip("-").isdigit() == False:
            return "Numero ingresado no válido, tiene que ser positivo"
        else:
            numeroint = int(numero)
    print("Adios")
def main():
    menu()

if __name__ == "__main__":
    main()