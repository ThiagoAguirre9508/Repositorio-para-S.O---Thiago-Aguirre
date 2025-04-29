dia = int(input("Ingrese un dia del 1 al 7: "))

if dia == 1:
    print("Lunes. Dia laboral")
elif dia == 2:
    print("Martes. Dia laboral")
elif dia == 3:
    print("Miercoles. Dia laboral")
elif dia == 4:
    print("Jueves. Dia laboral")
elif dia == 5:
    print("Viernes. Dia laboral")
elif dia == 6:
    print("Sabado. Fin de semana")
elif dia == 7:
    print("Domigo. Fin de semana")
elif dia >= 8:
    print("Numero invalido")