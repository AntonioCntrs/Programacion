#Contreras Osuna Jose Antonio 240053 "Hospital"
#En un hospital existen tres areas: ginecologia, traumatoliga y pedriatia. El presupuesto anual del hospital
#se reparte conforme a la siguiente tabla:
#   Ginecologia: 40%
#   Traumatologia: 30%
#   Pediatria: 30%
#obtener la cantidad de dinero que recibira cada area, para cualquier monto presupuestal.
pres=float(input("Dime cual es presupuesto de este ano:"))
gin=pres*.40
trau=pres*.30
ped=pres*.30
print("El presupuesto de este ano es:")
print(f"Ginecologia: {gin}")
print(f"Traummatologia: {trau}")
print(f"Pediatria: {ped}")