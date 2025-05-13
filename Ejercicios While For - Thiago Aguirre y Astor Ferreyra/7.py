pos = 0
neg = 0
prompos = 0
promneg = 0

for i in range(10):
    num = int(input("Ingrese un numero: "))
    if num >= 0:
        pos += 1
        prompos += num
    else:
        neg += 1
        promneg += num
prompos = prompos / pos
promneg = promneg / neg

print("Hay", pos, "numeros positivos y", neg, "numeros negativos.")
print("El promedio de los positivos es", prompos, "y el promedio de los negativos es", neg)