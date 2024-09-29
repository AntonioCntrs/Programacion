# Contreras Osuna Jose Antonio 240053 "Cociente y restos"
# Escribir un programa que pida al usuario dos números enteros
# y muestre por pantalla:
# a. La <n> entre <m> da un cociente <c> y un resto <r>.
# b. Donde <n> y <m> son los números introducidos por el
# usuario.c. Y <c> y <r> son el cociente y el resto de la división entera
# respectivamente.
n = int(input("Introduce el primer número entero (n): "))
m = int(input("Introduce el segundo número entero (m): "))
c = n // m
r = n % m
print(f"La {n} entre {m} da un cociente {c} y un resto {r}.")
