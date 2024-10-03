# Contreras Osuna Jose Antonio #240053
edad=int(input("Ingrese su edad: "))
if edad> 0 and edad<=6:
    print("Estas en la infancia :)")
else:
    if edad>6 and edad <= 12:
        print("Estas en la ninez")
    else:
        if edad>12 and edad<=20:
            print("Estas en la adolecencia :(")
        else:
            if edad>20 and edad<=25:
                print("Estas en la juventud")
            else:
                if edad>25 and edad<=60:
                    print("Estas en la adultez :(")
                else:
                    if edad>60:
                        print("Estas en la ancianidad:(")
                    else:
                        print("Ingrese una edad valida")
