def simbolos(numero):
    resultado = ""
    for i in range(1, numero + 1):
        resultado += '*' * i + "\n"
    return resultado
def main():
    numero = int(input("Ingresa numero: "))
    print(simbolos(numero))

if __name__ == "__main__":
    main()