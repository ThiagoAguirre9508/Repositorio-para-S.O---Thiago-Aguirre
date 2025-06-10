total=0
cont=0

while True:
    cargas = int(input("Ingrese distintas cargas de combustible (0 para cerrar el programa): "))
    
    if cargas == 0:
        break
    elif cargas < 5:
        print("se sospecha de error o recarga mínima")
        total = total + cargas
        cont=cont+1
    else:
        total = total + cargas
        cont=cont+1
    
prom=total/cont

print("El total de cargas realizadas es de: ", cont, ", habiendo sido un total de ", total, " litros, y su promedio es ", prom)