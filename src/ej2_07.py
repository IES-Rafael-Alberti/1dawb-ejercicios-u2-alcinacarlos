renta_anual = float(input("Introduce tu renta anual: "))
if renta_anual < 10000:
    tipo_impositivo = 0.05
elif renta_anual < 20000:
    tipo_impositivo = 0.15
elif renta_anual < 35000:
    tipo_impositivo = 0.20
elif renta_anual < 60000:
    tipo_impositivo = 0.30
else:
    tipo_impositivo = 0.45

print("El tipo impositivo que te corresponde es del", tipo_impositivo * 100, "%.")