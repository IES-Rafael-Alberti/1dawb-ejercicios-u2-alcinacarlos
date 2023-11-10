def buscar_letra(frase, letra):
    posicion = 0
    for caracter in frase:
        if caracter == letra:
            print(f"La letra '{letra}' se encuentra en la posición {posicion}.")
            return
        posicion += 1

    print(f"No está'{letra}' en la frase.")

def main():
    frase = input("Ingresa una frase: ")
    letra = input("Ingresa una letra a buscar: ")
    buscar_letra(frase, letra)

if __name__ == "__main__":
    main()