# Contreras Osuna Jose Antonio #240053
n=int(input("Ingrece un numero entero de mas de 1 digito "))
if n<10:
    print("mayor de dos digitos por favor")
else:
   numero_cadena= str(n)
   longitud_cadena= len(numero_cadena)
   print(f"la longitud es de {longitud_cadena}")
