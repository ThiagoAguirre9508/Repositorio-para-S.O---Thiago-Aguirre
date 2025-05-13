temp = 0
neg = 0
mayor = 0


print("Ingrese -100 para parar.")
while True:
    temp = int(input("Ingrese una temperatura: "))
    if temp == -100:
        break
    if temp < 0:
        neg += 1
    elif temp >= 30:
        mayor += 1

    
print("Hubo", neg, "temperaturas negativas y", mayor, "mayores o iguales a 30.")