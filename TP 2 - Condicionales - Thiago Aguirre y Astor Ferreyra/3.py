lista = []

while True:
    print("1. Agregar tarea")
    print("2. Ver lista")
    print("3. Cambiar estado")
    print("4. Eliminar tarea")
    print("5. Cancelar")
    num = int(input(""))

    if num == 1:
        nombre = input("Ingrese el nombre de la tarea: ")
        lista.append({"descripcion": nombre, "estado":"pendiente"})
        print("Tarea añadida exitosamente.")
    elif num == 2:
        print("lista: ")
        for i, t in enumerate(lista):
            print(f"{i+1}. {t['descripcion']} - Estado: {t['estado']}")
    
    elif num == 3:
        numero = int(input("Ingrese la tarea a actualizar: "))
        if 0 <= numero < len(lista):
            estado2 = input("Nuevo estado (pendiente / en proceso / completada):")
            lista[num]["estado"] = estado2
            print("Estado actualizado.") 
        else:
            print("Tarea inválida.")

    elif num == "4":
        numero = int(input("Ingrese el número de la tarea a eliminar: ")) - 1
        if 0 <= numero < len(lista):
            lista.pop(num)
            print("Tarea eliminada.")
        else:
            print("Número inválido.")

    elif num == "5":
        print("Saliendo del organizador de lista.")
        break
    else:
        print("Opción inválida.")