print("(1) Hamburguer")
print("(2) Pizza")
print("(3) Ensalada")
print("(4) Salir")
num = int(input(""))

if num == 1:
    print("Eligio hamburguesa")
elif num == 2:
    print("Eligio pizza")
elif num == 3:
    print("Eligio ensalada")
elif num == 4:
    print("Eligio salir")
elif num >= 5:
    print("Numero invalido")