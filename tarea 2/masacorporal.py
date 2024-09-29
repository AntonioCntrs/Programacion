# Contreras Osuna Jose Antonio 240053 "Masa corporal"
# Escribir un programa que pida al usuario su peso (en kg) y
# estatura (en metros), calcule el índice de masa corporal y lo
# almacene en una variable, y muestre por pantalla la frase:
# a. Tu índice de masa corporal es <imc>, donde <imc> es el
# índice de masa corporal calculado redondeado con dos
# decimales.


peso = float(input("Introduce tu peso en kg: "))
estatura = float(input("Introduce tu estatura en metros: "))
imc = peso / (estatura**2)
print(f"Tu índice de masa corporal es {imc:.2f}")
