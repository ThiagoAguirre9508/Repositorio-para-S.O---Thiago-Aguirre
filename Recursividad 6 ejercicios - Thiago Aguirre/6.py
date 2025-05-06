num=int(input("Ingrese un número: "))

i=10
aux2=0

while i<=num:
    aux=num%10
    num=num//10
    aux2=aux2*10+aux
aux2=aux2*10+num
print("El numero invertido será: ", aux2)