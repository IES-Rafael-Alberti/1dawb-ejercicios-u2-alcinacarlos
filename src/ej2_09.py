edad = int(input("Introduce tu edad: "))

if edad < 4:
    precio_entrada = 0
elif edad >= 4 and edad <= 18:
    precio_entrada = 5
else:
    precio_entrada = 10

print("Precio de la entrada es de", precio_entrada, "€.")