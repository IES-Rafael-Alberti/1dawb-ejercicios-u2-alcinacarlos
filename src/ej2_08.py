def leer_puntuacion(puntuacion): 
    nivel_rendimiento = ""
    cantidad_dinero = 2400
    if puntuacion == 0.0:
        nivel_rendimiento = "Inaceptable"
        cantidad_dinero = 0.0
    elif puntuacion == 0.4:
        nivel_rendimiento = "Aceptable"
        cantidad_dinero = 2400 * puntuacion
    elif puntuacion >= 0.6:
        nivel_rendimiento = "Meritorio"
        cantidad_dinero = 2400 * puntuacion
    else:
        print("Puntuación no válida.")
    return nivel_rendimiento, cantidad_dinero
    

def main():
    puntuacion = float(input("Introduce tu puntuación (0.0, 0.4, 0.6 o más): "))
    print(f"Cantida de dinero a recibir: {leer_puntuacion(puntuacion)[1]}")
    print(f"Nivel de rendimiento: {leer_puntuacion(puntuacion)[0]}")

if __name__ == "__main__":
    main()