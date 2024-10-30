#Contreras Osuna Jose Antonio #240053
def calcular_area_circulo(radio):
    pi = 3.141592653589793
    return pi * radio ** 2

while True:
    print("Selecciona una opción:")
    print("1. Calcular el área de un círculo")
    print("2. Salir")
    choice = input("Ingresa tu elección (1/2): ")

    if choice == '1':
        radio = float(input("Ingresa el radio del círculo: "))
        print(f"El área del círculo con radio {radio} es {calcular_area_circulo(radio):.2f}.\n")
    elif choice == '2':
        print("¡Adiós!")
        break
    else:
        print("Opción no válida. Por favor, intenta de nuevo.\n")