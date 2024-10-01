# Contreras Osuna Jose Antonio #240053
n1=int(input("Ingrece el primero numero entero: "))
n2=int(input("Ingrece el segundo numero entero: "))
if n1>n2:
    max=n1
    min=n2
else:
    if n2>n1:
        max=n2
        min=n1
    else:
        max=n1
        max=n2
dif=max-min
print(f"el Resultado de la diferencia es {dif}")     