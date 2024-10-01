# Contreras Osuna Jose Antonio #240053
n1=int(input("Ingrece el primero numero entero: "))
n2=int(input("Ingrece el segundo numero entero: "))
n3=int(input("Ingrece el tercer numero entero: "))
if n1>n2 and n1>n3:
    max=n1
else:
        if n2>n3:
         max=n2
        else:
         max=n3
print(f"El numero mas grande es {max}")
        