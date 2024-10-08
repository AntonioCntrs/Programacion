# Contreras Osuna Jose Antonio #240053
n=int(input("Ingrece un numero entero no negativo: "))
if n<0:
    print("Ingrece un numero no negativo")
else:
    fact=1
    for i in range( 1, n + 1):
        fact *= i   
    print(f"El resultado es {fact}") 
