dia = ("Ingrese el dia: ")
mes = ("Ingrese el mes: ")
año = ("Ingrese el año: ")

if dia > 0 and dia < 30 :
    print("Mañana es:", dia+1, mes, año)
else: 
    if mes > 0 and mes < 12 :
        print("Mañana es:", 1, mes+1, año)
    else:
        print("Mañana es:", 1, 1, año+1)