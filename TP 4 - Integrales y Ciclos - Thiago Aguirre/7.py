cont=0
cont2=0
mayor=0
total=0

for i in range(7):
    temp=int(input("ingrese la temperatura maxima en un dia: "))
    total=total+temp
    cont=cont+1
    if mayor < temp:
        mayor=temp
    if temp > 30:
        cont2=cont2+1
    
prom=total/cont
print("La media de temperatura es de ", prom,", la mayor temperatura fue de ", mayor,", y ", cont2, " dias se superaron los 30°")