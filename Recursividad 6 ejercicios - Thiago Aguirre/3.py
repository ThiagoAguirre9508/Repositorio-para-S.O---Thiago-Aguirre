b = 2
for i in range(1,29):
    cont=0

    for a in range(2, b//2):
        if b%a==0:
            cont=cont+1
            a=b
    if cont==0:
        print("el cubo de ", b, " es: ", b**3)
    b=b+1