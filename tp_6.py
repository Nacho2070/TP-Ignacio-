#TP 6
#Ejercicios 1-2-3-4
def values(): 
 numbers=[]
 while True:
     number=int(input("Ingrese numeros a la lista para salir 0: "))
     if number == 0 :
         break
     else:
        numbers.append(number)
     print(numbers)
 return numbers
 
def search_values(numbers): 
 search=int(input("ingrese un numero para buscarlo en la lista"))
 if search in numbers:
   numbers.remove(search)
 else:
   print("No fue posible eliminarlo")
 

def limit_number(numbers):
    
 sum=0
 for j in range(len(numbers)):
    sum +=  numbers[j] 
 limit_Number=int(input("Ingrese un numero limite: "))
 new_numbers=[]
 for x in numbers:
    if x < limit_Number:
        new_numbers.append(x) 
 print(f"Suma de todos los elemtos de la lista{sum}")
 print(f"Lista duplicada con valores menores a {limit_Number} : {new_numbers}")    
                    
number=values()                   
search_values(number)                    
limit_number(number)                    
print(f"Lista sin el primer numero que se brusco {number}")
