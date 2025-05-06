cont=0
x=0
num=0

print("Ingrese 10 numeros: ")

for i in range(1, 10+1):
    num=int(input("ingrese un número: "))

    if num%2==0:
        cont=cont+1

print("hay ", cont, " numeros pares")