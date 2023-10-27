def tipo_impositivo(renta_anual):
    if renta_anual < 10000:
        tipo_impositivo = "5%"
    elif renta_anual < 20000:
        tipo_impositivo = "15%"
    elif renta_anual < 35000:
        tipo_impositivo = "20%"
    elif renta_anual < 60000:
        tipo_impositivo = "30%"
    else:
        tipo_impositivo = "45%"
    return tipo_impositivo

def main():
    renta_anual = float(input("Introduce tu renta anual: "))
    print("El tipo impositivo es:", tipo_impositivo(renta_anual))

if __name__ == "__main__":
    main()