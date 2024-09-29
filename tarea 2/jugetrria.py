# Contreras Osuna Jose Antonio 240053 "jugeteria"
# Una juguetería tiene mucho éxito en dos de sus productos:
# payasos y muñecas. Suele hacer venta por correo y la empresa
# de logística les cobra por peso de cada paquete así que deben
# calcular el peso de los payasos y muñecas que saldrán en cada
# paquete a demanda. Cada payaso pesa 112g y cada muñeca
# 75g.

# a. Escribir un programa que lea el número de payasos y
# muñecas vendidos en el último pedido y calcule el peso
# total del paquete que será enviado.
# b. ¿Cuánto se cobrará de envío, si la paquetería cobra 120
# pesos por cada 600g?

peso_payaso = 112  # en gramos
peso_muneca = 75   # en gramos

num_payasos = int(input("Introduce el número de payasos vendidos: "))
num_munecas = int(input("Introduce el número de muñecas vendidas: "))

peso_total = (num_payasos * peso_payaso) + (num_munecas * peso_muneca)

costo_envio = ((peso_total + 599) // 600) * 120

print(f"El peso total del paquete es {peso_total} gramos.")
print(f"El costo de envío es {costo_envio} pesos.")


