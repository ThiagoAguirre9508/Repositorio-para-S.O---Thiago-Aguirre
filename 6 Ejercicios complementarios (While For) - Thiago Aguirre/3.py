primero = 2
lim=1000
cont=0

for i in range(primero, lim): #toma el rango, 2-1000
    primo=True
    valor=2

    while(i>valor)and primo==True:
        if i%valor == 0:
            primo=False
            break
        else:
            valor=valor+1

    if primo==True:
        print(i, "es primo")
        cont=cont+1

print("entre ", primero, " y ", lim, " hay ", cont, "numeros primos")