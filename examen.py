# Contreras osuna Jose Antonio #240053
# En un grupo de 15 alumnos de UPBC, se busca nombrar un jefe de grupo
# mediante el voto de cada uno de ellos. Todo esto en precencia de su
# maestro asesor. Sedecidio la votacion. Los 3 canditados son:
# 1.hugo; 2.paco y 3. luis
# El maestro asesor les solicito que el primer lugar sera jefe de grupo y el 
# segundo lugar ser tesorero.
# A) Queremos saber quien sera el jefe de grupo, con cuantos votos y porcetaje
# B) = = = = = = = = = = = = = = = tesoro ==============================
# C) al 3r lugar le daremos las gracias
i=0
j=0
hugo=0
paco=0
luis=0
nhugo=0
npaco=0
nluis=0
while True:
    while i<15:
        print("****Votacion para Jefe de grupo****")
        print("Ingrece la opcion deceada con un numero entero: ")
        print(" 1.Hugo ")
        print(" 2.Paco ")
        print(" 3.Luis ")
        voto=int(input("Seleccion: "))
        if voto == 1:
            hugo += 1
            i +=1
        elif voto == 2:
            paco += 1
            i += 1
        elif voto == 3:
            luis += 1
            i += 1
        else:
            print("Ingrece un numero entero por favor")
    phugo=(hugo*100)/15
    ppaco=(paco*100)/15
    pluis=(luis*100)/15

    if hugo>paco and hugo>luis:
        if paco>luis :
            print(f"Hugo es el jefe de grupo con {hugo} votos y un porcentaje de {phugo:.2f} % de votos")
            print(f"Paco es el tesorero con {paco} votos y un porcentaje de {ppaco:.2f} % de votos")
            print("Gracias por participar luis")
            break
        elif luis>paco:
            print(f"Hugo es el jefe de grupo con {hugo} votos y un porcentaje de {phugo:.2f} % de votos")
            print(f"Luis es el tesorero con {luis} votos y un porcentaje de {pluis:.2f} % de votos")
            print("Gracias por participar paco")
            break
        elif paco==luis:
            while j<15:
                print("Paco y luis empataron, haremos una votacion con ellos dos: ")
                print("1. Paco")
                print("2. Luis")
                nvoto=int(input("Ingrece su seleccion en un numero entero: "))
                if nvoto==1:
                    npaco += 1
                    j += 1
                elif nvoto==2:
                    nluis += 1
                    j += 1
                else:
                    print("Ingece un numero entero valido")
            if npaco>nluis:
                nppaco=(npaco*100)/15
                print(f"Hugo es el jefe de grupo con {hugo} votos y un porcentaje de {phugo:.2f} % de votos")
                print(f"Paco es el tesorero del grupo con {npaco} votos en el desempate y un porcentaje de {nppaco:.2f} % de votos ")
                print("Gracias por participar Luis :)")
                break
            else:
                npluis=(nluis*100)/15
                print(f"Hugo es el jefe de grupo con {hugo} votos y un porcentaje de {phugo:.2f} % de votos")
                print(f"Luis es el tesorero del grupo con {nluis} votos en el desempate y un porcentaje de {npluis:.2f} % de votos ")
                print("Gracias por participar Paco :)")
                break
    elif paco>hugo and paco>luis:
        if hugo>luis :
            print(f"Paco es el jefe de grupo con {paco} votos y un porcentaje de {ppaco:.2f} % de votos")
            print(f"Hugo es el tesorero con {hugo} votos y un porcentaje de {phugo:.2f} % de votos")
            print("Gracias por participar luis")
            break
        elif luis>hugo:
            print(f"Paco es el jefe de grupo con {paco} votos y un porcentaje de {ppaco:.2f} % de votos")
            print(f"Luis es el tesorero con {luis} votos y un porcentaje de {pluis:.2f} % de votos")
            print("Gracias por participar Hugo")
            break
        elif hugo==luis:
            while j<15:
                print("Hugo y luis empataron, haremos una votacion con ellos dos: ")
                print("1. Hugo")
                print("2. Luis")
                nvoto=int(input("Ingrece su seleccion en un numero entero: "))
                if nvoto==1:
                    nhugo += 1
                    j += 1
                elif nvoto==2:
                    nluis += 1
                    j += 1
                else:
                    print("Ingece un numero entero valido")
            if nhugo>nluis:
                nphugo=(nhugo*100)/15
                print(f"Paco es el jefe de grupo con {paco} votos y un porcentaje de {ppaco:.2f} % de votos")
                print(f"Hugo es el tesorero del grupo con {nhugo} votos en el desempate y un porcentaje de {nphugo:.2f} % de votos ")
                print("Gracias por participar Luis :)")
                break
            else:
                npluis=(nluis*100)/15
                print(f"Paco es el jefe de grupo con {paco} votos y un porcentaje de {ppaco:.2f} % de votos")
                print(f"Luis es el tesorero del grupo con {nluis} votos en el desempate y un porcentaje de {npluis:.2f} % de votos ")
                print("Gracias por participar Hugo :)")
                break
    elif luis>hugo and luis>paco:
        if hugo>paco :
            print(f"Luis es el jefe de grupo con {luis} votos y un porcentaje de {pluis:.2f} % de votos")
            print(f"Hugo es el tesorero con {hugo} votos y un porcentaje de {phugo:.2f} % de votos")
            print("Gracias por participar Paco")
            break
        elif paco>hugo:
            print(f"Luis es el jefe de grupo con {luis} votos y un porcentaje de {pluis:.2f} % de votos")
            print(f"Paco es el tesorero con {paco} votos y un porcentaje de {ppaco:.2f} % de votos")
            print("Gracias por participar Hugo")
            break
        elif hugo==paco:
            while j<15:
                print("Hugo y Paco empataron, haremos una votacion con ellos dos: ")
                print("1. Hugo")
                print("2. Paco")
                nvoto=int(input("Ingrece su seleccion en un numero entero: "))
                if nvoto==1:
                    nhugo += 1
                    j += 1
                elif nvoto==2:
                    npaco += 1
                    j += 1
                else:
                    print("Ingece un numero entero valido")
            if nhugo>npaco:
                nphugo=(nhugo*100)/15
                print(f"Luis es el jefe de grupo con {luis} votos y un porcentaje de {pluis:.2f} % de votos")
                print(f"Hugo es el tesorero del grupo con {nhugo} votos en el desempate y un porcentaje de {nphugo:.2f} % de votos ")
                print("Gracias por participar Paco :)")
                break
            else:
                nppaco=(npaco*100)/15
                print(f"Luis es el jefe de grupo con {luis} votos y un porcentaje de {pluis:.2f} % de votos")
                print(f"Paco es el tesorero del grupo con {npaco} votos en el desempate y un porcentaje de {nppaco:.2f} % de votos ")
                print("Gracias por participar Hugo :)")
                break
    elif hugo==paco or hugo==luis:
        print("Hubo algun empate, haremos la votacion de nuevo, voten diferente por favor")
        i=0
    elif paco==luis or paco==hugo:
        print("Hubo algun empate, haremos la votacion de nuevo, voten diferente por favor")
        i=0