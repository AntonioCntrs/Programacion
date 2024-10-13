# Contreras Osuna Jose Antonio #240053
i=0
p=0
ng=0
z=0
while i<10:  
    n=float(input("Ingrece un numero: "))
    if n<0:
        ng+=1
        i+=1
    elif n>0:
        p+=1
        i+=1
    elif n==0:
        z+=1
        i+=1
print(f"Hay {p} positivos, {ng} negativos y {z} ceros")