def par_impar(numero):
    if numero % 2 == 0:
        return f"{numero} es par."
    else:
        return f"{numero} es impar."
    
def main():
    numero = int(input("Introduce un número entero: "))
    print(par_impar(numero))

if __name__ == "__main__":
    main()