def calcular_total():
    total = 0
    monto = int(input("Ingrese la compra (0 para finalizar): "))
    while monto != 0:
        if monto < 0:
            print("No puede ser negativo")
        else:
            total += monto
        monto = int(input("Ingrese la compra (0 para finalizar): "))
    
    if total > 1000:
        descuento = total - (total * 0.10)
        print(f"El total a pagar es: ${descuento}.")
    else:
        print(f"El total a pagar es: ${total}")

def main():
    calcular_total()

if __name__ == "__main__":
    main()