# 1. Escribir un programa que pregunte al usuario por el número de
# horas trabajadas y el coste por hora.
# a) Después debe mostrar por pantalla la paga que le
# corresponde.
hora=float(input("Ingrese horas trabajadas:"))
pago=float(input("Ingrese su salario por hora:"))
salario=hora*pago
print(f"Su salario correspondiente es: {salario}")