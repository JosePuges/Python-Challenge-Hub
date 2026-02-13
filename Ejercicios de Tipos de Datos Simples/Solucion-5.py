# Escribir un programa que pregunte al usuario por el número 
# de horas trabajadas y el coste por hora. 
# Después debe mostrar por pantalla la paga que le corresponde.

horas = float(input("Horas trabajadas: "))
coste = float(input("Coste por hora: "))
paga = horas * coste

print("La paga es: ", paga)