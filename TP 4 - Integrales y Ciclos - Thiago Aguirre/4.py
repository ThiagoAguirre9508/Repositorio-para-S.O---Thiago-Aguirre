cont=0
cont2=0

for i in range(10):
    nota = int(input("Ingrese una nota de un alumno: "))
    
    if nota >= 7:
        cont=cont+1
    elif nota < 7:
        cont2=cont2+1

print("Hay ", cont," alumnos aprobados y ", cont2, " desaprobados")