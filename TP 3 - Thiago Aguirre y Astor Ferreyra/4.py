import random
rando = random.randint(1, 10)

for i in range(3):

    num = int(input("Ingrese el número que cree que  el programa eligió (de 1 a 10): "))
    
    if num == rando:
        print("Numero correcto")
        break
    elif i==2:
        print("Intentos agotados, el numero era ", rando)
    else:
        print("Numero equivocado, intentelo de nuevo")