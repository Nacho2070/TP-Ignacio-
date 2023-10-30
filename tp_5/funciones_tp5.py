#Ejericicio 1
def check_DNI(dni):
  
  if len(dni)==7 or len(dni)==8:
    return True
  else:
    return False
#Ejercicio2

def length_word(world):
 #we use split
  new_world=world.split()
 #we access to last word
  last_world=new_world[-1]
  print(len(last_world))

#Ejercicio 3

def get_name(name): 
 fragmento_name=name.split()
 first_name=fragmento_name[0]
 return first_name

def get_dni(dni):
    while True:
      if len(dni) == 8 or len(dni)== 7 :
        return dni 
      else:
         print("Dni incorrecto")

def get_id(dni):
  dni_cadena=str(dni)
  id = dni_cadena[:3]
  new_id = int(id)
  return new_id

#Ejecicio 4

def ask_For_a_Number(number,number_2):
 
  if number % number_2 == 0:
       print(f"{number} es múltiplo de {number_2}")
  else:
       print(f"{number} no es múltiplo de {number_2}")

#Ejercicio 5

def medium_Temperature(max_Temp,min_Temp):
   medium_Temp=(max_Temp-min_Temp)/2
   return medium_Temp


