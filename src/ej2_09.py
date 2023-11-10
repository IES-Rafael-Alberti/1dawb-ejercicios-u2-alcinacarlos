def calcular_precio(edad):
    if edad < 4:
        precio_entrada = 0
    elif edad >= 4 and edad <= 18:
        precio_entrada = 5
    else:
        precio_entrada = 10
    return precio_entrada

def main():
    edad = int(input("Introduce tu edad: "))
    print("Precio de la entrada es de", calcular_precio(edad), "€.")

if __name__ == "__main__":
    main()