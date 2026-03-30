nombre=input("Cliente: ").strip()

while nombre == "" or not nombre.isalpha():
    print ("Error: ingresa un nombre no vacio y solo con letras")
    nombre = input("Cliente: ").strip()

cantidad_str=input("Ingresa la cantidad de productos: ").strip()

while not cantidad_str.isdigit() or int(cantidad_str) == 0:
    print("Error: ingresa un numero entero o positivo mayor a cero")
    cantidad_str = input("Ingresa la cantidad de productos: ").strip()

cantidad_int = int(cantidad_str)

total_sin_descuento = 0
total_con_descuento = 0

for i in range (1, cantidad_int+1):
    precio_str = input(f"Producto {i} - Precio: ").strip()

    while not precio_str.isdigit() or int(precio_str) <= 0:
        print("Error: el precio debe ser un entero positivo")
        precio_str = input(f"Producto {i} - Precio: ").strip()

    precio_int = int(precio_str)

    total_sin_descuento += precio_int

    desc=input("Descuento (S/N): ").strip().lower()

    while desc != "s" and desc != "n":
        print ("Error: ingrese S para si o N para no")
        desc = input("Descuento (S/N): ").strip().lower()

    if desc == "s":
        precio_final = precio_int * 0.9
    else:
        precio_final = precio_int

    total_con_descuento += precio_final

ahorro = total_sin_descuento - total_con_descuento
promedio = total_con_descuento / cantidad_int

print(f"Total sin descuentos: ${total_sin_descuento}")
print(f"Total con descuentos: ${total_con_descuento:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")