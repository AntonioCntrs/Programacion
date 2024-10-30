#Contreras Osuna Jose Antonio #240053
def minutos_a_horas(minutos):
    horas = minutos // 60
    minutos_restantes = minutos % 60
    return horas, minutos_restantes

def horas_a_minutos(horas, minutos):
    return horas * 60 + minutos

while True:
    print("Selecciona una opción:")
    print("1. Convertir minutos a horas")
    print("2. Convertir horas a minutos")
    print("3. Salir")
    choice = input("Ingresa tu elección (1/2/3): ")

    if choice == '1':
        minutos = int(input("Ingresa la cantidad de minutos: "))
        horas, minutos_restantes = minutos_a_horas(minutos)
        print(f"{minutos} minutos son {horas} horas y {minutos_restantes} minutos.\n")
    elif choice == '2':
        horas = int(input("Ingresa la cantidad de horas: "))
        minutos = int(input("Ingresa la cantidad de minutos: "))
        total_minutos = horas_a_minutos(horas, minutos)
        print(f"{horas} horas y {minutos} minutos son {total_minutos} minutos.\n")
    elif choice == '3':
        print("¡Adiós!")
        break
    else:
        print("Opción no válida. Por favor, intenta de nuevo.\n")