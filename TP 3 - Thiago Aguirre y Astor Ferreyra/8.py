par = 0

for i in range(5):
    num = int(input("Ingrese un numero: "))
    if num % 2 == 0:
        par += 1
    
if par > 0 :
    print("Hay uno o mas numeros pares.")
else:
    print("No hay numeros pares.")