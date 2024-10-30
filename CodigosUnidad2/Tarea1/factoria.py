def factorial(n):
    if n == 0:
        return 1
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

numero = int(input("Introduce un número entero no negativo: "))
print(f"El factorial de {numero} es {factorial(numero)}")