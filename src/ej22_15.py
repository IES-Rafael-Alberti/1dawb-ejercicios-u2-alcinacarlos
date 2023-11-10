def sumatoria():
    numeros = []
    resultadonum = 0
    numero = input()
    if numero.strip("-").isdigit() == False:
        return "Pon un número válido"
    else:
        numero = int(numero)
    
    while numero != 0:
        if numero > 0:
            resultadonum += numero
            numeros.append(numero)
        numero = input()
        if numero.strip("-").isdigit() == False:
            return "Pon un número válido"
        else:
            numero = int(numero)
    resultado = " + ".join(map(str, numeros))
    resultado += " = " + str(resultadonum)
    return resultado
    

def main():
    print(sumatoria())

if __name__ == "__main__":
    main()