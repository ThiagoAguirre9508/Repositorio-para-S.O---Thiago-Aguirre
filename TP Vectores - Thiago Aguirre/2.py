suma=0
temp=[]
i=1
C=0
media=0.0

N=int(input("Ingrese el numero de temperaturas a ingresar: "))

for i in range(N):
    temperatura = float( input("Ingrese Temperatura {0}: ".format(i + 1) ))
    temp.append(temperatura)
    suma=suma+temperatura

media=suma/N

for tempElement in temp:
    if tempElement >= media:
        C = C + 1
        print(tempElement)

print("La media es de ", media, ", y el total de temperaturas mayores o iguales a la media es de ", C)