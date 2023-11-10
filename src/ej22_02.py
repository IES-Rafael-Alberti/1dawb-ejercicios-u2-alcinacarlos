def años_cumplidos(edad):
    resultado = ""
    for año in range(1, edad + 1):
        resultado += "Has cumplido {} años".format(año) + "\n"
    return resultado

def main():
    edad = int(input("Ingresa tu edad: "))
    print(años_cumplidos(edad))

if __name__ == "__main__":
    main()