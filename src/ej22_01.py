def imprimir_10(palabra):
    resultado = ""
    for i in range(10):
        resultado += palabra+ "\n"
    return resultado
        
def main():
    palabra = input("Introduce una palabra: ")
    print(imprimir_10(palabra))
        
if __name__ == "__main__":
    main()