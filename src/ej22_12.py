def contar_veces(frase, letra):
    resultado = 0
    contador = 0
    while contador != len(frase):
        if frase[contador] == letra:
            resultado += 1
        contador += 1
    if resultado == 0:
        return "No aparece la letra en la frase"
    else:
        return f"La letra aparece {resultado} veces en la frase"

def main():
    frase = input("Introduce una palabra: ")
    letra = input("Introduce una letra: ")
    print(contar_veces(frase, letra))

if __name__ == "__main__":
    main()