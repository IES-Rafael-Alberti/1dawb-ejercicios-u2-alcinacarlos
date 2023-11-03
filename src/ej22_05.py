def cuenta_atras(cantidad_invertir, num_años, interes_anual):
    resultado = ""
    for año in range(1, num_años + 1):
        cantidad_invertir *= 1 + (interes_anual / 100)
        resultado += f"Año {año}: {cantidad_invertir:.2f} €\n"
    return resultado

def main():
    cantidad_invertir = int(input("Cantidad a invertir: "))
    num_años = int(input("Número de años: "))
    interes_anual = int(input("Interés anual (%): "))
    print(cuenta_atras(cantidad_invertir, num_años, interes_anual))

if __name__ == "__main__":
    main()