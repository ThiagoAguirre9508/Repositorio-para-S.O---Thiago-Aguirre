costo = int(input("Ingrese el costo del articulo: "))
marca = int(input("Ingrese la marca: "))
precio = 0

if costo > 2000 and marca == "NOSY":
    precio = costo * 0.9
    precio = precio * 0.95
    print("El precio final es: ", precio)

elif costo < 2000 and marca == "NOSY":
    precio = costo * 0.95
    precio = precio + precio * 0.20
    print("El precio final es: ", precio)

elif costo > 2000 and marca != "NOSY":
    precio = costo * 0.9
    print("El precio final es: ", precio)


elif costo < 2000 and marca != "NOSY":
    precio = costo * 1.20
    print("El precio final es: ", precio)