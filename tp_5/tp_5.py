from funciones_tp5 import *

 #Ejercicio 1

dni=input("Ingrese su numero de dni")
value=check_DNI(dni)
print(value)

#Ejercicio 2

world=input("Ingresa una frase").lower()
length_word(world)

#Ejercicio 3
while True:
 name=input("Ingrese su nombre: ")
 if len(name) > 0:
  dni=input("Ingrese su dni: ")
  show_Name=get_name(name)
  show_Dni=get_dni(dni)
  show_id=get_id(dni)
 else:
  break

 print (f"Nombre: {show_Name} DNI: {show_Dni} ID: {show_id}")
 print("Si deseea salir deje en nombre en blanco y presione Enter: ")

#Ejericio 4

 number=input("Ingrese el primer numero")
 number_2=input("Ingrese el segundo numero")
ask_For_a_Number(number,number_2)

#Ejercicio 5
days = int(input("Introduza la cantidad de dias para calcular su temperatura media"))
timer=0
while timer < days:
 print(f"dia{timer+1}")
 min = int(input("Introduza la temperatura minima"))
 max = int(input("Introduza la temperatura maxima"))
 medium= medium_Temperature(max,min)
 print(f"La temperatura media es de: {medium}")
 timer=timer+1
 

