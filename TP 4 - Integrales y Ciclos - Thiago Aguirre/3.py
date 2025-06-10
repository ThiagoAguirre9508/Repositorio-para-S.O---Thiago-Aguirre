cont=0
cont2=0
total=1
i=1
for i in range(7):
    cant=int(input("Ingrese la cantidad de vasos de agua que toma en un día: "))
    cont=cont+1
    total=cant+total
    if cant <8:
        cont2=cont2+1

prom=total/cont

if cont2 >0:
    print("Su promedio diario es de ", prom, ", y se le recomienda aumentar el consumo de agua")
else:
    print("Su promedio diario es de ", prom)