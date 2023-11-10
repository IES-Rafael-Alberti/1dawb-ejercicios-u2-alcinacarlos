def eco():
    salir = "salir"
    palabra = input()
    while palabra != salir:
        print(palabra)
        palabra = input()

def main():
    eco()

if __name__ == "__main__":
    main()