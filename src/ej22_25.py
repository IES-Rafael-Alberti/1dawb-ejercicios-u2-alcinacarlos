def palabra_larga():
    frase = input("Ingresa una frase: ")
    palabras = frase.split(" ")
    max_len = -1
    for palabra in palabras:
        if len(palabra) > max_len:
            max_len = len(palabra)
            resultado = palabra
    cantidad_palabras = len(palabras)
    print(f"Palabra más larga: {resultado}")
    print(f"Cantidad de palabras: {cantidad_palabras}")

def main():
    palabra_larga()
    
if __name__ == "__main__":
    main()
