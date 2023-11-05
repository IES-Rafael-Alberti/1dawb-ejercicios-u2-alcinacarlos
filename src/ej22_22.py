def contar_digitos():
    total_pares = 0
    total_impares = 0

    numero = int(input("Ingrese un número entero positivo (0 para finalizar): "))

    while numero != 0:
        if numero < 0:
            print("El número debe ser positivo. Intente nuevamente.")
        else:
            pares = 0
            impares = 0
            numero_str = str(numero)

            for digito in numero_str:
                if int(digito) % 2 == 0:
                    pares += 1
                else:
                    impares += 1

            print(f"El número {numero} tiene {pares} dígitos pares y {impares} dígitos impares.")

            total_pares += pares
            total_impares += impares

        numero = int(input("Ingrese un número entero positivo (0 para finalizar): "))

    print(f"Total de dígitos pares leídos: {total_pares}")
    print(f"Total de dígitos impares leídos: {total_impares}")

def main():
    contar_digitos()

if __name__ == "__main__":
    main()
