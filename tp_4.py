#Ejercicio 1

lines = []
while True:
    line = input("Ingrese una linea o presione Enter para finalizar:")
    if not line:
        break  
    lines.append(line)

for line in lines:
    print(line.upper())

#Ejercicio 2
bank_deposit = 0
while True:
    print("Indique la operación a realizar: ")
    opcion = input("Presione 'd' para depositar dinero o 'r' para retirar dinero: ").lower()
    amount = int(input("Ingrese el monto a depositar/retirar: "))
    
    if opcion == 'd':
        bank_deposit += amount
    elif opcion == 'r':
        bank_deposit -= amount
    
    exit = input("Si desea salir, presione Enter. De lo contrario, presione cualquier otra tecla: ")
    if not exit :
        break

print("Saldo en la cuenta bancaria:", bank_deposit)
#Ejercicio 3

contnumbers = 0
while True:
 number = int(input("Ingrese numeros.."))
 print("Si deseea salir presione 0")
 if number == 0:
  break
 if number % number == 0:
       print("No es primo")
 else:
    contnumbers += 1
    
print("La cantidad de numnero primos fue de: ",contnumbers)
"""
"""""
#Ejercicio 4
year1=int(input("Ingresa el año de  inicio"))
year2=int(input("Ingresa el año de fin.."))
bisiesto = []
print("Rango de años entre ",year1," y ",year2)
for year in range(year1,year2+1):

 print(year)

 if (year % 4 == 0 and year % 100 != 0) or year % 400==0:
    
    bisiesto.append(year)

for year in bisiesto:
  if year % 10 == 0:
    print(year) 
   
#Ejercicio 5

for num in range(20):
    if num % 2 == 0:
      print(num)  
    else:
       continue
#Ejercicio 6
number_list = [1,14,56,7,8,90,55,36]
number_found = 0
for search in number_list:
 if search == 90 :
   number_found = search
   break

print("Numero encontrado ",number_found)
  
#Ejecicio 7
while True:
    print("Menú:")
    print("1) Deposito de dinero")
    print("2) Retirar dinero")
    print("3) Pedir préstamo")
    print("0) Salir")

    selection = int(input("Ingrese el número para seleccionar una opción: "))

    if selection == 1:
        print("Seleccionaste: Depósito de dinero")
    elif selection == 2:
        print("Seleccionaste: Retiro de dinero")
    elif selection == 3:
        print("Seleccionaste: Pedir préstamo")
    elif selection == 0:
        print("Saliendo...")
        break
    else:
        print("Opción no válida. Por favor, elige una opción válida.")