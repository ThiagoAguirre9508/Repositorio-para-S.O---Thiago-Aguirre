ingresos = float(input("Ingrese sus ingresos: "))
gastos = float(input("Ingrese sus gastos: "))

saldo = ingresos - gastos

porcentaje = gastos / ingresos * 100

print("El saldo restante es: ", saldo)
print("Se uso ", porcentaje, "% de los ingresos.")