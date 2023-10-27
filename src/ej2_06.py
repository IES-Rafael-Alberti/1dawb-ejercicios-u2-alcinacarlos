def grupo_corresponde(nombre, sexo):
    nombre = nombre.upper()
    if (sexo == "M" and nombre < "M") or (sexo == "H" and nombre >= "N"):
        return "A"
    else:
        return "B"
    
    
def main():
    nombre = input("Introduce tu nombre: ")
    sexo = input("Introduce tu sexo: ")
    print(grupo_corresponde(nombre, sexo))

if __name__ == "__main__":
    main()