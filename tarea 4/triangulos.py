# Contreras Osuna Jose Antonio #240053
l1=float(input("Ingrese el lado 1: "))
l2=float(input("Ingrese el lado 2: "))
l3=float(input("Ingrese el lado 3: "))
if l1==l2 and l2==l3:
    print("Tu triangulo es equilatero")
else:
    if l1!=l2 and l2!=l3 and l1!=l3:
        print("Tu triangulo es escaleno")
    else:
        print("Tu triangulo es isoceles")