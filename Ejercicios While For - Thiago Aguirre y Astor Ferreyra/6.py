password="Coradir2025"

for i in range(3):
    passw= str(input("Ingrese su contraseña: "))
    
    if passw == password:
        print("Contraseña correcta")
        break
    elif i == 2:
        print("Acceso bloqueado, numero de intentos alcanzado")
    else:
        print("Intentelo de nuevo")