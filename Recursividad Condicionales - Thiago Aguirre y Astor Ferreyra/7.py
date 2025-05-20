pi = 3.1416 
print("1-Circulo")
print("2-Triangulo")

num = int(input(""))

if num == 1:
    L = input("Ingrese el lado del triangulo: ")
    A = ((3 ** 0.5)/4) * L
    print("El area es: ", A)
elif num == 2:
    R = input("Ingrese el radio del circulo: ")
    C = pi * R ** 2
    print("La circunferencia es: ", C)
else:
    print("Error")
