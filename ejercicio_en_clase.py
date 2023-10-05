

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#we ask the phrase 5 times
for i in range(5):
    words = input(f"Ingrese la frase {i + 1}: ").lower()
    size = int(input("Ingrese la cantidad de posiciones a recorrer: "))
    newword = ""
    newchar = ""
#we go through each letter of the phrase
    for x in words:    
        if x in alphabet:
            newchar = alphabet[(alphabet.index(x) + size) % 27]
            newword += newchar
       #If the word has numbers we save it
        else:  
            newword += x
    print("Frase modificada:", newword)

#Ejercicio 2
    print("Ingresa números. Si deseas salir, introduce 0")
cont_numberpares = 0
cont_numberimpares = 0
while True:
 number=int(input("Numero: "))
 if number == 0:
    break
 if number % 2 == 0:
    cont_numberpares += 1  
 else:
    cont_numberimpares += 1
print("La cantidad de numeros pares fue de ",cont_numberpares," y la cantidad de numeos impares fue de : ",cont_numberimpares)
