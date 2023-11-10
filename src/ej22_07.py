def tabla_multiplicar():
    resultado = ""
    for multiplicando in range(1, 11):
        resultado += f"Tabla de multiplicar del {multiplicando}:\n"
        
        for multiplicador in range(1, 11):
            resultadomult = multiplicando * multiplicador
            resultado += f"{multiplicando} x {multiplicador} = {resultadomult}\n"
        resultado += "\n"
    return resultado

def main():
    print(tabla_multiplicar())

if __name__ == "__main__":
    main()