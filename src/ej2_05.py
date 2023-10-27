edad = int(input("Introduce tu edad: "))
ingresos_mensuales = float(input("Introduce tus ingresos: "))

if edad > 16 and ingresos_mensuales >= 1000:
    print("Debes tributar.")
else:
    print("No debes tributar.")