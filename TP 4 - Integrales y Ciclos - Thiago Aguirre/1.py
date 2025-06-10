lim = int(input("Ingrese el limite presupuestado para los gastos del mes: "))
total=0
gasto=1

while gasto != 0:
    gasto = int(input("Ingrese los gastos del mes continuamente (0 para cerrar el programa): "))
    if gasto==0:
        break
    else:
        total = total + gasto

if lim > total:
    print("El total gastado (", total, ") NO supera el limite presupuestado (", lim, ")")
elif lim < total:
    print("El total gastado (", total, ") supera el limite presupuestado (", lim, ")")
elif lim == total:
    print("El total gastado (", total, ") es igual al limite presupuestado (", lim, ")")