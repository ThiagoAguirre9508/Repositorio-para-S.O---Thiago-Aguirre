
nfinal = 0

for i in range (5):
    nota = int(input("Ingrese su nota: "))
    nfinal = nota + nfinal
    
prom = nfinal/5

if prom >= 7:
        
    print("Su promedio (", prom, ") supera 7")

else:
    print("Su promedio (", prom, ") no supera 7")