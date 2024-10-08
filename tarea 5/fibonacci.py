# Contreras Osuna Jose Antonio #240053
n=int(input("Ingrece el numero de veces que desea repetir la serie de fibonacci "))
if n<0:
    print("mayor de dos digitos por favor")
else:
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b
  