#TP 6
#Ejercicios 1-2-3-4
numbers=[]
while True:
     number=int(input("Ingrese numeros a la lista para salir 0: "))
     if number == 0 :
         break
     else:
        numbers.append(number)
     print(numbers)
search=int(input("ingrese un numero para buscarlo en la lista"))

if search in numbers:
    numbers.remove(search)
else:
 print("No fue posible eliminarlo")
sum=0
for j in range(len(numbers)):
    sum +=  numbers[j] 
limit_Number=int(input("Ingrese un numero limite: "))
new_numbers=[]
for x in numbers:
    if x < limit_Number:
        new_numbers.append(x) 
                    
print(f"Lista sin el primer numero que se brusco {numbers}")
print(f"Suma de todos los elemtos de la lista{sum}")
print(f"Lista duplicada con valores menores a {limit_Number} : {new_numbers}")