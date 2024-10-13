# Contreras Osuna Jose Antonio #240053
s=1
print(f" {s} elefante se columpiaba")
while s<10:  
    n=int(input("Cuantos elefantes se columpiaban?: "))
    if n == s+1:
        s+=1
        print(f" {s} elefante se columpiaba")
    else:
        print("Intente de nuevo por favor")
print("Son todos los elefantes :)")