edad = int(input("Ingrese su edad: "))

if edad < 18:
    print("Usted es menor de edad.")
elif edad >= 18 and edad <= 64:
    print("Usted es adulto.")
elif edad >= 65:
    print("Usted es adulto mayor.")