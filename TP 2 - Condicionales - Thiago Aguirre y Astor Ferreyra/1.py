cuenta = int(input("Ingrese el total de la cuenta a pagar: "))
porcent = int(input("Ingrese el porcentaje de propina que desea dejar: "))

monto=cuenta*(porcent / 100)
total=monto+cuenta

print("El total a pagar será de ", total, ", siendo la propina de ", monto)