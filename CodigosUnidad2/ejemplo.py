def sumar_cinco_numeros(a,b,c,d,e):
    suma = a+b+c+d+e   
    return suma

resultado= sumar_cinco_numeros(2,3,4,5,8)
print("La suma es: ",resultado)

def promedio(resultado):
    prom=resultado/5
    return prom

resultado_promedio=promedio(resultado)
print(f"El promedio es: {resultado_promedio:.2f}")

from ejemplo_nombre import imprima
name= input("ingrece su nombre: ")
nombre=imprima(name)

from carpeta.espar import espar_
numero=int(input("Ingrece un numero"))
par=espar_(numero)
print(par)