contraseña = "contraseña"
def verificar_contraseña(input_usuario):
    while input_usuario != contraseña:
        print("Contraseña incorrecta. Vuelve a intentarlo")
        if __name__ != "__main__":
            #para las pruebas unitarias
            return False
        else:
            input_usuario = input("Introduce la contraseña: ")
    return "Contraseña Correcta"

def main():
    input_usuario = input("Introduce la contraseña: ")
    print(verificar_contraseña(input_usuario))

if __name__ == "__main__":
    main()