stock = int(input("Ingrese el Stock del producto a controlar: "))
alerta=stock*0.10
print(alerta)
while stock != 0:
    cant=int(input("Ingrese la cantidad de producto vendido: "))
    stock=stock - cant

    if stock < alerta:
        print("ALERTA: el Stock está siendo de menos de su 10% original (quedan ", stock," productos)")
    if stock <=0:
        break
print("programa finalizado")