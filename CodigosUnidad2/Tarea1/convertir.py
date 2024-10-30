#Contreras Osuna Jose Antonio   240053
def convertir_distancia():
    valor = float(input("Introduce la distancia: "))
    unidad = input("Introduce la unidad ('km' para kilómetros, 'mi' para millas): ").strip().lower()

    if unidad == 'km':
        resultado = valor * 0.621371
        unidad_convertida = 'mi'
    elif unidad == 'mi':
        resultado = valor / 0.621371
        unidad_convertida = 'km'
    else:
        print("Unidad no válida.")
        return

    print(f"{valor} {unidad} son {resultado:.2f} {unidad_convertida}")
convertir_distancia()