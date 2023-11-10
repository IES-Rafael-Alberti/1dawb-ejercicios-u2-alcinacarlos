def alreves_una_a_una(input_usuario):
    input_usuario = input_usuario[::-1]
    resultado = ""
    contador = 0
    while contador != len(input_usuario):
        resultado += input_usuario[contador] + "\n"
        contador += 1
    return resultado

def main():
    input_usuario = input("Introduce una palabra: ")
    print(alreves_una_a_una(input_usuario))

if __name__ == "__main__":
    main()