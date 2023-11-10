def sumatoria():
    contador = 0
    resultado = 0
    numero = input()
    if numero.isdigit() == False:
        return "Numero ingresado no válido, tiene que ser positivo"
    
    while contador != len(numero):
        resultado += int(numero[contador])
        contador += 1
    return resultado
    

def main():
    print(sumatoria())

if __name__ == "__main__":
    main()