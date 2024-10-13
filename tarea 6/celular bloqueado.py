# Contreras Osuna Jose Antonio #240053
i=0
while i<3:  
    n=float(input("Ingrece PIN de 4 digitos "))
    if n != 3519:
        i+=1
        if i==3:
            print("Llamando a la policia >:(")
            break
        else:
            print("Intente de nuevo")   
    else:
        print("Login Correcto :)")
        break


