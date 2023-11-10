def es_primo(input_usuario):
    for n in range(2, input_usuario):
        if input_usuario % n == 0:
            return "No es primo"
    return "Es primo"

def main():
    input_usuario = int(input("Introduce un numero: "))
    print(es_primo(input_usuario))

if __name__ == "__main__":
    main()