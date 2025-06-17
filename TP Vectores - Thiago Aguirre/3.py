vector=[]

n=int(input("Ingrese la cantidad de elementos para esta lista (maximo de 200): "))

if n <=200:
    for i in range(1, n+1):
        elemento=int(input("Ingrese el elemento (1): ".format(i+1)))
        vector.append(elemento)

    i=0
    ordenado=[]
    for elemento in vector:
        if elemento not in ordenado:
            ordenado.append(elemento)

            ordenado.sort()

    print(ordenado)

else:
    print("Número de valores equivocado")    