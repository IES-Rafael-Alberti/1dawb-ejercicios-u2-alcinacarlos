def impares(numero):
    resultado = ""
    for i in range(1, numero + 1, 2):
        resultado += str(i) + ", "
    resultado = resultado[:-2]
    return resultado
def main():
    numero = int(input("Ingresa numero entero positivo: "))
    print(impares(numero))

if __name__ == "__main__":
    main()