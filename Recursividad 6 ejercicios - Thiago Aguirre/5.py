num=int(input("Ingrese un numero: "))
s=0
for x in range(1, num+1):
    if x%2 == 0:
        s=s-(1/x)
    else:
        s=s+(1/x)

print("La suma será: ", s)