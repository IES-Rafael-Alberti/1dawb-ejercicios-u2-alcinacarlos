def contar_digitos():
    digitos = 0
    lineas = 0
    libro = input("LIbro: ")
    while libro != "*":
        for letra in libro:
            if letra.isdigit():
                digitos += 1
        if libro == "/":
            print(f"Línea completa. Aparecen {digitos} dígitos numéricos.")
            digitos = 0
            lineas += 1
        libro = input("LIbro: ")
    print(f"Fin. Se leyeron {lineas} líneas completas.")

def main():
    contar_digitos()
    
if __name__ == "__main__":
    main()
