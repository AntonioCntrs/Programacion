# Contreras Osuna Jose Antonio #240053
sum=0
while True:  
    n=float(input("Ingrece el precio de su producto: "))
    if n == 0:
        break
    elif n<0:
        print("Ingrece un nuevo monto por favor: ")
    else:
        sum += n
if sum>1000:
    sum = sum -(sum*.1)
    print(f"Su total con descuento es de {sum}")
else:
    print(f"Su total es de {sum}")
