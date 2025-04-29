saldo = int(input("Ingrese el valor de su saldo: "))
monto = int(input("Ingrese el monto que va a retirar: "))

if monto <= saldo:
    print("el saldo restante es de ", saldo-monto)
elif monto > saldo:
    print("Fondos insuficientes")