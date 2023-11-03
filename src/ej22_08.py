def triangulo(numero):
    resultado = ""
    for i in range(1, numero + 1):
        for i in range(i * 2 - 1, 0, -2):
            resultado += str(i) + " "
        resultado += "\n"
    return resultado

def main():
    numero = int(input("Introduce un numero: "))
    print(triangulo(numero))

if __name__ == "__main__":
    main()