from funcion import *
number_2=0

while True:
  number=int(input("Ingrese numero: "))
  #add the digits
  number_2 += number
  addition=summation(number_2)
  print (number_2)
  if number == 0:
    break

print(f"Suma de los numeros: {number_2} Suma de lo digitos {addition}")
