total=0
precio=1

while precio != 0:
    precio = int(input("Ingrese el precio de su producto (0 para terminar): "))
    
    total=precio+total

if precio > 10000:
    descuento = total *0.1
    print("Se le aplicará un descuento del 10%, por lo que el total es de: ", total-descuento )
else:
    print("Su valor total es de: ", total)
