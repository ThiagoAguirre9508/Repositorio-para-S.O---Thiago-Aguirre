lim = 20000
gasto=1

while gasto != 0:
    gasto = int(input("Ingrese cuanto gasto en esta compra: "))
    lim=lim-gasto
    if lim<=0:
        print("usted ya no puede realizar mas compras")
        break