# Contreras Osuna Jose Antonio #240053
x=int(input("Ingrece un numero entero no negativo: "))
i=0
if x<0:
    print("Ingrece un numero no negativo")
else:
    for i in range( 1, 11):
        x1=x*i
        print(f"{x} X {i} = {x1}")
        
