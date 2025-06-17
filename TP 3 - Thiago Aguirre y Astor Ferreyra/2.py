edad = 1

niños=0
adoles=0
adultos=0

while edad != 0:
    edad = int(input("Ingrese su edad (0 para terminar): "))
    
    if edad <13 and edad>0:
        niños= niños+1
    elif edad >= 13 and edad <=17:
        adoles=adoles+1
    elif edad >= 18:
        adultos= adultos+1
    elif edad == 0:
        break

print("En las edades ingresadas, hay ", niños , " niños, ", adoles, " adolescentes, y ", adultos, " adultos")