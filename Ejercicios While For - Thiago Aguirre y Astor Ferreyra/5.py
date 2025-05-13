primo = 0
num = int(input("Ingrese un número: "))

if num >= 1:
    for i in range(2, num):
        if num % i == 0:
            print("El numero no es primo.")
            primo = 1
            break
    if primo == 0:
        print("El numero es primo.")