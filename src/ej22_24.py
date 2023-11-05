from ej22_10 import es_primo
def cantidad_primos():
    primos = 0
    numero = int(input("Introduce un numero: "))
    while numero != 0:
        if numero <= 1:
            numero = int(input("Introduce un numero mayor que 1: "))
        else:
            if es_primo(numero) == "Es primo":
                primos += 1
        numero = int(input("Introduce un numero: "))
    print(f"Cantidad de primos: {primos}")




def main():
    cantidad_primos()
    
if __name__ == "__main__":
    main()
