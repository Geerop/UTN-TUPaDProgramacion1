
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

operador = input("Ingrese su nombre: ")

while not operador.isalpha():
    operador = input("Error. Ingrese solo letras: ")

opcion = ""

while opcion != "6":
    print("Menú")
    print("1. Reservar turno.")
    print("2. Cancelar turno.")
    print("3. Ver agenda del día.")
    print("4. Ver resumen general.")
    print("5. Cerrar sistema.")
    
    opcion = input("Elija una opción: ")
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 5:
        opcion = input("Opción inválida. Intente nuevamente con un número del 1 al 5: ")
    if opcion == "1":
        dia = ""
        dia = input("Elegir día (1= Lunes, 2= Martes): ")

        while dia != "1" and dia != "2":
            dia = input("Error. Elegir día 1 o 2: ")

        nombre = operador
    
        if dia == "1":
                    if nombre == lunes1 or nombre == lunes2 or nombre == lunes3 or nombre == lunes4:
                        print("Ese paciente ya tiene turno el lunes.")
                
                    elif lunes1 == "":
                        lunes1 = nombre
                        print("Se ha reservado el primer turno del lunes.")
                    elif lunes2 == "":
                        lunes2 = nombre
                        print("Se ha reservado el segundo turno del lunes.")
                    elif lunes3 == "":
                        lunes3 = nombre
                        print("Se ha reservado el tercer turno del lunes.")
                    elif lunes4 == "":
                        lunes4 = nombre
                        print("Se ha reservado el cuarto turno del lunes.")
                    else:
                        print("No hay turnos disponibles el lunes.")       
    
        if dia == "2":
                    if nombre == martes1 or nombre == martes2 or nombre == martes3:
                        print("Ese paciente ya tiene turno el martes.")
                    elif martes1 == "":
                        martes1 = nombre
                        print("Se ha reservado el primer turno del martes.")
                    elif martes2 == "":
                        martes2 = nombre
                        print("Se ha reservado el segundo turno del martes.")
                    elif martes3 == "":
                        martes3 = nombre
                        print("Se ha reservado el tercer turno del martes.")
                    else: 
                        print("No hay turnos disponibles el martes.")   


    elif opcion == "2":

        dia = input("Elegir día (1= Lunes, 2= Martes): ")
        while dia != "1" and dia != "2":
            dia = input("Error. Elegir día 1 o 2: ")

        nombre = input("Nombre del paciente: ")
        while not nombre.isalpha():
            nombre = input("Error. Solo se admiten letras: ")
        
        if dia == "1":
                    if lunes1 == nombre:
                        lunes1 = ""
                        print("Turno cancelado")
                    elif lunes2 == nombre:
                        lunes2 = ""
                        print("Turno cancelado")
                    elif lunes3 == nombre:
                        lunes3 = ""
                        print("Turno cancelado")
                    elif lunes4 == nombre:
                        lunes4 = ""
                        print("Turno cancelado")
                    else:
                        print("Paciente no encontrado")
        if dia == "2":
                    if martes1 == nombre:
                        martes1 = ""
                        print("Turno cancelado")
                    elif martes2 == nombre:
                        martes2 = ""
                        print("Turno cancelado")
                    elif martes3 == nombre:
                        martes3 = ""
                        print("Turno cancelado")
                    else:
                        print("Paciente no encontrado")
    elif opcion == "3":
        dia = input("Elegir día (1= Lunes, 2= Martes): ")
        while dia != "1" and dia != "2":
            dia = input("Error, elegir día 1 o 2: ")
        
        if dia == "1":
                        print("\nAgenda del Lunes:")
                        print("Turno 1:", lunes1 if lunes1 != "" else "(libre)")
                        print("Turno 2:", lunes2 if lunes2 != "" else "(libre)")
                        print("Turno 3:", lunes3 if lunes3 != "" else "(libre)")
                        print("Turno 4:", lunes4 if lunes4 != "" else "(libre)")
        if dia == "2":   
                        print("\nAgenda del Martes:")
                        print("Turno 1:", martes1 if martes1 != "" else "(libre)")
                        print("Turno 2:", martes2 if martes2 != "" else "(libre)")
                        print("Turno 3:", martes3 if martes3 != "" else "(libre)")

    elif opcion == "4":
        ocupados_lunes = 0
        ocupados_martes = 0
                    
        if lunes1 != "":
            ocupados_lunes += 1
        elif lunes2 != "":    
            ocupados_lunes += 1
        elif lunes3 != "":
            ocupados_lunes += 1
        elif lunes4 != "":
            ocupados_lunes += 1
            
        elif martes1 != "":
            ocupados_martes += 1
        elif martes2 != "":
            ocupados_martes += 1
        elif martes3 != "":
            ocupados_martes += 1
    
        libres_lunes = 4 - ocupados_lunes
        libres_martes = 3 - ocupados_martes

        print("\n--- RESUMEN ---")
        print("Lunes: ocupados =", ocupados_lunes, "|libres =", libres_lunes)
        print("Martes: ocupados =", ocupados_martes, "|libres =", libres_martes)

        if ocupados_lunes > ocupados_martes:
            print("Día con más turnos ocupados: Lunes")

        elif ocupados_martes > ocupados_lunes:
            print("Día con más turnos ocupados: Martes")

        else:
            print("Hay empate en cantidad de turnos")    
    
    elif opcion == "5": 
        print("Cerrando sistema...")
        break