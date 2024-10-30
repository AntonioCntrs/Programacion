#Conteras Osuna Jose Antonio #240053
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0/9.0

def celsius_to_fahrenheit(celsius):
    return (celsius * 9.0/5.0) + 32

while True:
    print("Selecciona una opción:")
    print("1. Convertir Fahrenheit a Celsius")
    print("2. Convertir Celsius a Fahrenheit")
    print("3. Salir")
    choice = input("Ingresa tu elección (1/2/3): ")

    if choice == '1':
        f_temp = float(input("Ingresa la temperatura en Fahrenheit: "))
        print(f"{f_temp} grados Fahrenheit son {fahrenheit_to_celsius(f_temp):.2f} grados Celsius.\n")
    elif choice == '2':
        c_temp = float(input("Ingresa la temperatura en Celsius: "))
        print(f"{c_temp} grados Celsius son {celsius_to_fahrenheit(c_temp):.2f} grados Fahrenheit.\n")
    elif choice == '3':
        print("¡Adiós!")
        break
    else:
        print("Opción no válida. Por favor, intenta de nuevo.\n")