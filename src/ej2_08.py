puntuacion = float(input("Introduce tu puntuación (0.0, 0.4, 0.6 o más): "))

nivel_rendimiento = ""
cantidad_dinero = 2400

if puntuacion == 0.0:
    nivel_rendimiento = "Inaceptable"
    cantidad_dinero = 0.0
    print("Tu nivel de rendimiento es:", nivel_rendimiento)
    print("Recibirás", cantidad_dinero, "€.")
elif puntuacion == 0.4:
    nivel_rendimiento = "Aceptable"
    cantidad_dinero = 2400 * puntuacion
    print("Tu nivel de rendimiento es:", nivel_rendimiento)
    print("Recibirás", cantidad_dinero, "€.")
elif puntuacion >= 0.6:
    nivel_rendimiento = "Meritorio"
    cantidad_dinero = 2400 * puntuacion
    print("Tu nivel de rendimiento es:", nivel_rendimiento)
    print("Recibirás", cantidad_dinero, "€.")
else:
    print("Puntuación no válida.")