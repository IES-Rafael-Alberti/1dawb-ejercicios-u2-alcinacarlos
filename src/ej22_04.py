def cuenta_atras(numero):
    resultado = ""
    for i in range(numero, -1, -1):
        resultado += str(i) + ", "
    resultado = resultado[:-2]
    return resultado
def main():
    numero = int(input("Ingresa numero entero positivo: "))
    print(cuenta_atras(numero))

if __name__ == "__main__":
    main()