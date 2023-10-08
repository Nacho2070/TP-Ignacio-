#Ejecicio 1

word = input("Ingrese una palabra: ")
for i in range(10):
    print(word)
 
 #Ejercicio 2
years =int(input("Ingrese su edad: "))

for cont in range(years):
    print(cont+1)
#Ejecicio 3
number =int(input("Ingrese un numero entero positivo: "))
print("Rango de numeros impares de",number)
for cont in range(number):
    if cont % 2 != 0 :
      print(cont)

      #Ejecicio 4
positive_number=int(input("Ingrese un numero entero positivo: "))

if positive_number > 0 :
      for x in range(positive_number):
        print(positive_number)
        positive_number -= 1
   
else:
    print("El numero debe ser   positivo")
#Ejercicio 5
amount_to_invest=int(input("Cantidad a invertir "))
annual_interest=int(input("Intereses anuales "))
number_of_years=int(input("Cantidad  de años a  invertir "))
total = amount_to_invest
for year in range(1,number_of_years):
    total += (total * annual_interest) /100
    print(f"Año{year}: {total:.2f}")
   
 
#Ejercicio 6

triangle=int(input("Ingresa el tamaño de un triangulo: "))
asterisk = "*"
print(asterisk)
for size in range(triangle):
     asterisk = asterisk + "*"
     print(asterisk)

#Ejercicio 7
i = 1
n=  1
for i in range(11):
     print("Tabla del ",i)
     for n in range(11):
      print(i,"x",n,"=",i*n)
#Ejerciio 8
import random
number=int(input("Ingresa un numero para realizarun triangulo: "))

for i in range(5):
    for n in range(i,0,-1):
     
       print(n,end="")
    print()

#Ejericicio 9

password = "python2023"

while True:
 password_user = input("Introduzca la contraseña ")

 if password_user == password:
   print("Contraseña correcta")  
   break 
 else:
   print("Contraseña incorrecta,intentelo de nuevo")
#Ejercicio 10
number = int(input("Ingrese un numero entero para determinar si es o no primo"))
temp =True
if number <= 1:
  temp = False
else:  
 for i in range(2,number):
  if  i % number == 0:
    temp = False
    break
  
   
if  temp:
  print("Es primo")
else:
  print("No es primo")
""
""
#Ejercicio 11
word = input("Introdusca una palabra")
for x in word[::-1]:
  print(x)

#Ejercicio 12
phrase = input("Introduzca una frase")
letter = input("Introduzcua una letra")
cont = 0
for i in phrase:
  if letter == i:
    cont = cont + 1

print("La letra",letter,"aparece:",cont,"veces en la frase")
#Ejercico 13
while True:
  word=input("Introduzca una palabra").lower()
  print(word)
  if  word == "salir":
    break
#Ejecicio14
  n1=int(input("Introduzca un numero entero"))
  n2=int(input("Introduzca un numero entero"))
if n1 > n2:
    n1, n2 = n2, n1
for  number in range(n1,n2):
   if number % 2 == 0:
        print(f"{number} es par.")
   else:
        print(f"{number} es impar.")
#Ejericio 15
number = int(input("Ingrese un número entero mayor que cero: "))

if number <= 0:
    print("ingrese un número entero mayor que cero.")
else:
    print(f"Los divisores de {number} son:")
    for i in range(1, number + 1):
        if number % i == 0:
            print(i)
#Ejercicio 16

number_of_numbers = int(input("¿Cuántos números va a introducir? "))


negative_numbers = 0


for i in range(number_of_numbers):
    numero = float(input(f"Ingrese el número #{i + 1}: "))
    if numero < 0:
        negative_numbers += 1

print(f"Ha introducido {negative_numbers} número(s) negativo(s).")
#Ejercicio 17

phrase = input("Ingrese una frase: ").lower()
vocales = set()

vocales_total = "aeiou"

for letter in phrase:
    if letter in vocales_total:
        vocales.add(letter)

print("Vocales en la frase :")
for vocal in vocales:
    print(vocal)
#Ejercicio 18

a, b = 0, 1

for _ in range(10):
    print(a, end=" ")
    a, b = b, a + b

#Ejericio 19
aim = 500000
total =0
while True:
    amount=int(input("Igrese la cantidad de dinero para ahorrar"))
    total += amount
    if total >=  aim:
        print("A llegado a la  cantidad de dinero deseeado")
        break
#Ejericio 20
total = 0
while True:
    number=int(input("Ingrese numeros enteros para sumarlos para salir presione  0"))
    total += number
   
    if number == 0 :
        print("Saliendo...")
        break
print(f"La suma de los  numeros ingresados es de {total}")    

#Ejericio 21
bigger_number= 0
while True:
   number=int(input("Ingrese numeros enteros positivos ingrese 0 para salir"))
   if bigger_number < number:
      bigger_number = number
   if number == 0:
    break
 
print(f"El numero mayor es {bigger_number}")   
#Ejericio 22

even_numbers_count = 0

while True:
    number = int(input("Ingrese un  numero entero o -1 para salir: "))
    
    if number == -1:
        break
    
    if number <= 0:
        print("Ingrese un valor positivo")
        continue

    # Initialize the variable to store the sum of digits
    digit_sum = 0
    
    # Calculate the sum of digits
    absolute_number = abs(number)
    while absolute_number > 0:
        digit = absolute_number % 10
        digit_sum += digit
        absolute_number //= 10

    print(f"La  suma de  los digitos de {number} es {digit_sum}.")
    
    if number % 2 == 0:
        even_numbers_count += 1

print(f"Se ingresaron {even_numbers_count} numeros pares")
#Ejercicio 23
total = 0
while True:
 sales_money = float(input("Dinero de las ventas: "))
 print("Si  deseea salir presione el numero 0")
 if sales_money ==  0:
    break
 if sales_money <= 0 :
    print("Error debe ser un monto  positivo")
    continue
 if sales_money >= 1000:
    total += sales_money-(sales_money*0.10)
 else:
    total += sales_money 

print(f"Total a pagar {total}")
#Ejercicio 24

number = int(input("Ingresa un numero para su factorial "))
factorial = 1
if number < 0:
    print("No se puede calcular el factorial de un número negativo.")
elif number == 0:
    print("El factorial de 0 es 1.")
else:
 print(f"Factorial de {number}")
 for  i in range(1,number):
    factorial *= i 
    print(factorial)
