def division(dividendo, divisor):
    if divisor == 0:
        return "No se puede dividir entre cero."
    else:
        resultado = dividendo / divisor
        return f"El resultado de la división es: {resultado}"
    
def main():
    dividendo = int(input("Introduce el dividendo: "))
    divisor = int(input("Introduce el divisor: "))
    
    print(division(dividendo, divisor))


if __name__ == "__main__":
    main()