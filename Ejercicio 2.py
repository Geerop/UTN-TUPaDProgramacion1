usuario_correcto = "alumno"
contrasena_correcta = "python123"

intentos = 0
while intentos < 3:
    print(f"Intento {intentos+1}/3")

    usario_ingresado = input("Usuario: ")
    clave_ingresada = input("Clave: ")

    if usario_ingresado == usuario_correcto and  clave_ingresada == contrasena_correcta:
        print("Acceso concedido.")
        acceso = True
        break
    
    else:
        print("Error: credenciales inválidas.")
        intentos += 1

if not acceso:
    print("Cuenta bloqueada.")
else:
    while True:
        print("\n1)Estado. \n2)Cambiar clave. \n3)Mensaje. \n4)Salir.")  

        opcion = input("Opcion: ").strip()
        if not opcion.isdigit():
            print("Error: ingrese un numero valido.")
            continue
        opcion = int(opcion)
        if opcion == 1: 
            print("Inscripto.")
        elif opcion == 2:
            while True:
                nueva_clave = input("Ingrese la nueva clave: ")

                if len(nueva_clave) < 6:
                    print("Error: la contraseña debe tener un mínimo de 6 caracteres.")
                    continue
                else:
                    confirmacion = input("Confirmar clave: ")
                if nueva_clave == confirmacion:
                    contrasena_correcta = nueva_clave
                    print("Clave actualizada.")
                    break
                else:
                    print("Error: las claves no coinciden.")
        elif opcion == 3:
            print("No need to hurry. No need to sparkle. No need to be anybody but oneself. \n -Virginia Woolf.")
        elif opcion == 4:
            print("Cerrando sesión...")    
            break