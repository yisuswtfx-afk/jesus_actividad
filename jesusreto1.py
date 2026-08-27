nombre = input("Ingrese el nombre del empleado: ")
horas_trabajadas = int(input("Ingrese las horas trabajadas: "))
valor_hora = int(input("Ingrese el valor de cada hora: "))

salario = horas_trabajadas * valor_hora

print("Empleado:", nombre)
print("Horas trabajadas:", horas_trabajadas)
print("Valor hora: $", valor_hora)
print("Salario: $", salario)
