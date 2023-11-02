from mutantes import *
def llenar_valores():
 dni=[]
 dni_temp=[]
 cont = 0
 cont1=0
 cont2=0
 while True :
  
   letters = ["a", "t", "g", "c"]

   
   dni_temp_1=input("Ingrese una linea de letras 'A,T,G,C'").lower()
   dni_temp.append(dni_temp_1)
   
   if dni_temp in ("a" or "t" or "g" or "c") and len(dni_temp)==6:
      
      cont1+=1
      dni.append(dni_temp_1)
    
    
      print(f"Secuencia actual {dni}")
   else:
     print("La letra no es valida,prueba con otra")

   if len(dni)==36:
    break
 search_mutante(dni,letters)




def search_mutante(dni,letters):
  horizontally=[]
  vertical=[]
  for i in dni:
   for x in i:
     if x in letters:
       horizontally.append(x)
       if len(horizontally) > 4:
         break
       
  print(f"Secuencia horizontal:{horizontally} ")     

  for x in range(dni):
     if dni[x][0] in letters:
       vertical.append(dni[x][0])
       if len(vertical) > 4:
         break
       
 for 
