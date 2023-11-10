def tributar(edad, ingresos):
    if edad > 16 and ingresos >= 1000:
        return "Debes tributar"
    else:
        return "No debes tributar"
    
def main():
    edad = int(input("Introduce tu edad: "))
    ingresos_mensuales = float(input("Introduce tus ingresos: "))
    print(tributar(edad, ingresos_mensuales))

if __name__ == "__main__":
    main()