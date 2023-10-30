#TP 8
#Ejecicio 1

def positive_number(n):
 cont_digits=0
 while True:
   extNum = n % 10
   cont_digits+=1
   n //= 10
   if n == 0:
       return cont_digits


number=int(input("ingrese un numero para obtener la cantidad de digitos"))    
digits=positive_number(number)
print(digits)         

#Ejericio 2

def positive_number(n,b):
 # We handle the special case in which n is 1
 if n == 1:
        return True
 # We initialize a variable to store the current power.
 cont=1
 while cont <= n:
        if cont == n:
            return True
        
        cont *= b  
       #if no power equal to n is found, returns false
        return False

number_1=int(input("ingrese un numero para obtener la cantidad de digitos"))    
number_2=int(input("ingrese un numero para obtener la cantidad de digitos"))    

result=positive_number(number_1,number_2)
print(result)  

#Ejericio 3

def find_positions(a, b, start=0):
    # We initialize a list to store the found positions.
    positions = []

    # We search for the first occurrence of b in a starting from position 'start'.
    pos = a.find(b, start)

    # If no more occurrences are found, we return the current list
    if pos == -1:
        return positions

    
    positions.append(pos)

    return positions + find_positions(a, b, pos + 1)

a = "un tete a tete con Tete"
b = "te"
results = find_positions(a, b)
print(results) 