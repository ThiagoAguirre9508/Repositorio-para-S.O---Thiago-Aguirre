total=0
cont=0
mayor=0

while True:
    cant=int(input("Ingrese la cantidad que desea ingresar a la colecta: "))
    total=total+cant
    cont=cont+1
    if cant > mayor:
        mayor=cant
    if cant==0:
        cont=cont-1
        break

print("El total colectado es de ", total,", la cantidad de gente que aporto es de ", cont," , y la mayor donacion es de ", mayor)