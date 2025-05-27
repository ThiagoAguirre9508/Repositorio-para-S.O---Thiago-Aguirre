import random
import string

longitud = input("Ingrese la longitud de la contraseña: ")
numeros = input("Desea incluir numeros?(y/n): ")
letras = input("Desea incluir caracteres?(y/n): ")
simbolos = input("Desea incluir simbolos?(y/n): ")

contraseña = ""
valores = ""

if numeros == "y":
    valores += string.digits
if numeros == "y":
    valores += string.ascii_letters
if numeros == "y":
    valores += string.punctuation


contraseña = "".join(random.choice(valores) for i in range(longitud))
print("La contraseña es: ", contraseña)