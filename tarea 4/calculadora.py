# Contreras Osuna Jose Antonio #240053
print("Seleccione la operacion a realizar:")
print("1. suma")
print("2. resta")
print("3. multiplicacion")
print("4. division")
r=int(input("Seleccion: "))
if r==1:
    n1=float(input("Ingrese el primer numero: "))
    n2=float(input("Ingrese el segundo numero: "))
    r=n1+n2
    print(f"La suma de {n1} + {n2} es = {r}")
else:
    if r==2:
        n1=float(input("Ingrese el primer numero: "))
        n2=float(input("Ingrese el segundo numero: "))
        r=n1-n2
        print(f"La resta de {n1} - {n2} es = {r}")
    else:
        if r==3:
            n1=float(input("Ingrese el primer numero: "))
            n2=float(input("Ingrese el segundo numero: "))
            r=n1*n2
            print(f"La multiplicacion de {n1} * {n2} es = {r}")
        else:
            if r==4:
                n1=float(input("Ingrese el primer numero: "))
                n2=float(input("Ingrese el segundo numero: "))
                r=n1/n2
                print(f"La division de {n1} / {n2} es = {r}")
            else:
                print("Ingrese una opcion valida")
