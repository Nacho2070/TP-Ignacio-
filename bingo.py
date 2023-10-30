import random
def fill_Cardboard(bingo):
 
 horizontally=[]
 vertical=[]
 diagonal=[]
 exit_game = False

 
 while not exit_game:
    input("Presione enter para extraer un numero aleatorio")
    azar_nm = random.randint(1, 75)
    print(f"El numero es extraido es: {azar_nm}")
    # Search in the values horizontally
    for i in range(len(bingo)):
        for j in range(5):
            if bingo[i][j] == azar_nm:
                horizontally.append(azar_nm)
                if len(horizontally) == 5:
                    print(f"Bingo!! linea horizontal completa: {horizontally}")
                    exit_game = True    
                    break
                     

    # Search in the values vertically
    for i in range(5):
        for j in range(len(bingo)):
            if bingo[j][i] == azar_nm:
                vertical.append(azar_nm)
                if len(vertical) == 5:
                    print(f"Bingo!! linea vertical completa:{vertical}")
                    exit_game = True
                    break

    # Search in the value diagonal
    for x in range(len(bingo)):
        if bingo[x][x] == azar_nm:
            if len(diagonal) == 5:
                print(f"Bingo!! linea diagonal completa:{diagonal}")
                exit_game = True
                break     
#cardboard creation
def  create_bingo_cardboard():
   bingo=[]       
   bingo_2=[]
   repeated_numbers =set()           
   cont=0
   while cont < 5:
      cont+=1         
      cardboard =[]
      while len(cardboard ) < 5:
    
        bingo_2 = int(input(f"Ingrese números del 1 al 75 para llenar el cartón del bingo ({len(cardboard) + 1}/5): "))
        if bingo_2 in repeated_numbers:
            print("El número está repetido, prueba con otro.")
            continue
        #checking number ranges
        if 1 <= bingo_2 <= 75:
            cardboard .append(bingo_2)
            repeated_numbers.add(bingo_2)
        else:
            print("Error: el número debe estar en el rango de 1 a 75.")
       #we add our temporary list to "bingo"
      bingo.append(cardboard )  
      print("Cartón actual:", cardboard )
  
   return bingo     
  
#Main
while True:
 print("Bienvenido..")
 
 bingo=create_bingo_cardboard()
 
 fill_Cardboard(bingo)
 
 play_Again = input("Si deseea seguir jugando escriba 'si' de lo contrario escriba 'no'").lower()
 if play_Again != "si":    
      print("Saliendo del programa...")
      break
 