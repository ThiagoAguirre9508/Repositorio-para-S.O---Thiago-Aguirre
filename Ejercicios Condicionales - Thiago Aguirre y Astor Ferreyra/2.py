vel = int(input("Ingrese la velocidad de su vehiculo: "))

if vel <= 60:
    print("Usted está dentro del limite permitido ")
elif vel >= 61 and vel <= 80:
    print("Usted está en exceso leve, disminuya la velocidad")
elif vel > 80:
    print("Usted está en exceso grave, disminuya la velocidad inmediatamente")