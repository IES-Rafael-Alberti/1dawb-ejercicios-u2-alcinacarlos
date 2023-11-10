def ingresar_contraseña(contraseña):
    guardada = "contraseña"
    if contraseña.lower() == guardada:
        return "Contraseña correcta"
    else:
        return "Contraseña incorrecta"

def main():
    contraseña = input("Introduce la contraseña: ")
    print(ingresar_contraseña(contraseña))

if __name__ == "__main__":
    main()