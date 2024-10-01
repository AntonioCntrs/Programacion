# Contreras Osuna Jose Antonio #240053
n=int(input("Dame un numero entero de tres digitos"))
if 1 <= n <= 999:
        # Convertir el número a cadena, invertir la cadena y convertirla de nuevo a entero
     ni= int(str(n)[::-1])
else:
    print("El número debe estar en el rango de 1 a 999.")
print(f"El numero invertido de {n} es {ni}")
