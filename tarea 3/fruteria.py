# Contreras Osuna Jose Antonio #240053
print("Manzana $66 el Kilo")
kilos=float(input("Cuantos kilos de manzana compraste?"))
if kilos>0 and kilos<=2:
    precio=kilos*66
    print(f"El precio es de {precio}")
else:
    if kilos>2 and kilos<=5:
        precio=kilos*66
        precio=precio-(precio*.1)
        print(f"El precio es de {precio}")
    else:
        if kilos>=5.01 and kilos<=10:
            precio=kilos*66
            precio=precio-(precio*.15)
            print(f"El precio es de {precio}")
        else:
            if kilos>=10.01:
             precio=kilos*66
             precio=precio-(precio*.2)
             print(f"El precio es de {precio}")