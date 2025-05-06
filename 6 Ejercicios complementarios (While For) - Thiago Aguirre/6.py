print("Determinar valor y rango del primer termino que supere 300")
n1=1
n2=0
an=n1+(2*n2)
cont=0

while an < 300:
    n2=n1
    n1=an
    an=n1+(2*n2)
    cont=cont+1

print("El rango es ", cont, " y el resultado es ", an)
