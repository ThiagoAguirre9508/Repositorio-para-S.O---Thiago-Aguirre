c=-1 #capital
I=0 #Interés
m=0 #años

while (c<0) or (I<=0) or (I>=100) or (m<=0):
    c = int(input("Ingrese su capital: "))
    I = int(input("Ingrese el interés: "))
    m = int(input("Ingrese el tiempo en años: "))
    
for i in range(m):
    c = c*(1+I/100)

print("Tienes ", c, " pesos")