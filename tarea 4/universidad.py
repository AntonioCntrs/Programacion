# Contreras Osuna Jose Antonio #240053
print("Ingrese una opcion:")
print("1. Veterano")
print("2. Regular")
o=int(input("Opcion: "))
a=int(input("Ingrese el numero de asignaturas: "))
if o==1:
    p=a*30
    print(f"Usted es veterano y pagara {p} dolares por sus {a} asignaturas")
else:
    if o==2:
        p=a*50
        print(f"Usted es veterano y pagara {p} dolares por sus {a} asignaturas")
    else:
        print("Ingrece una opcion valida... ")