
n1 = int(input("Ingrese un número, uno negativo para cerrar el programa: "))
while n1 > 0:
    suma=0
    for i in range (1, n1+1):
        if n1 % i == 0:
            suma = suma + i

    print("La suma de los divisores del numero ", n1, " da como resultado: ", suma)
    n1 = int(input("Ingrese un número negativo para cerrar el programa: "))
    