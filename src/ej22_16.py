def sumatoria():
    numeros = []
    numero = input()
    if numero.isdigit() == False:
        return "Numero ingresado no válido, tiene que ser positivo"
    else:
        numero = int(numero)
    while numero != 0:
        numeros.append(numero)
        numero = input()
        if numero.isdigit() == False:
            return "Numero ingresado no válido, tiene que ser positivo"
        else:
            numero = int(numero)
    return max(numeros)
    

def main():
    print(sumatoria())

if __name__ == "__main__":
    main()