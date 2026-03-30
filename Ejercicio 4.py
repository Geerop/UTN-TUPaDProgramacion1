
nombre = input("Ingresa tu nombre de agente: ")
while not nombre.isalpha():
    nombre=input("Error. Ingrese solo letras: ")
    
    print(f"Bienvenido agente {nombre}.")

racha_forzar = 0
energia = 100
tiempo = 12
alarma = False
cerraduras_abiertas = 0
codigo_parcial = ""

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:
    print("Estado: ")
    print(f"Energía: {energia}.")
    print(f"Tiempo: {tiempo}.")
    print(f"Cerraduras abiertas: {cerraduras_abiertas}.")

    print("1. Forzar cerradura.")
    print("2. Hackear panel.")
    print("3. Descansar.")
    
    opcion = input("Elija una opción: ")
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
        opcion=input("Error. Ingrese un número válido: ") 
    if opcion == 1:
        energia -= 20
        tiempo -= 2
        racha_forzar += 1
        cerraduras_abiertas += 1
        print("Forzaste una cerradura.")
        if racha_forzar == 3:
            print("¡Forzaste demasiado! La cerradura se trabó.")
            alarma = True
            racha_forzar = 0
        if energia < 40:
            num = input("Riesgo de alarma! Elegí un número (1-3): ")

        while not num.isdigit() or int(num) < 1 or int(num) > 3:
            num = input("Error. Elegí un número entre 1 y 3: ")

        if int(num) == 3:
            alarma = True
        else:
            cerraduras_abiertas += 1

    elif opcion == 2:
        energia -= 10
        tiempo -= 3
        for i in range(4):
            print("Hackeando paso", i + 1)
            codigo_parcial += "A"
            if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
                cerraduras_abiertas += 1
                print("¡Código completo! Se abrió una cerradura.")
    elif opcion == 3:
        energia += 15
        if energia > 100:
            energia = 100
            tiempo -= 1
        if alarma:
            energia -= 10
            print(f"La alarma te afectó mientras descansabas, {energia}.")
    elif alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        print("El sistema se bloqueó por la alarma.")
        break
    elif energia <= 0 or tiempo <= 0:
        print("PERDISTE. Te quedaste sin recursos.")
    elif alarma:
        print("PERDISTE. Sistema bloqueado.") 
    elif cerraduras_abiertas == 3:
        print("¡GANASTE! Abriste la bóveda.")