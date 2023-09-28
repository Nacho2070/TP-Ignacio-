
# We ask a date
day_week = input("Ingrese un dia de la semana ").lower
dayint_week = int(input("Ingrese el numero del dia ").lower)
number_month =int(input("Ingrese el numero del mes "))
boolean = True 

if day_week not in ["lunes" "martes" "miercoles" "jueves" "viernes"]:
    boolean = False
if dayint_week < 1 or dayint_week > 10:
    boolean = False
if number_month < 1 or number_month > 12:
    boolean = False
#We check that the date is correct
if boolean :
 # We ask the user what day the exams were taken
    exam_day = input("Ingrese el dia en el que se tomaron los examenes: ").lower()
    #If it is equal to Monday, Tuesday or Wednesday, the percentage of approvals will be calculated
    if exam_day not in["lunes" "martes" "miercoles"]:
          alumnos_aprobados =int(print("Indique la cantidad de alumnos que aprobaron"))
          alumnos_desaprobados =int(print("Indique la cantidad de alumnos que desaprobaron"))
          total_alumn = alumnos_aprobados + alumnos_desaprobados
          porcentaje_aprob = (alumnos_aprobados/total_alumn)*100
          print(f"Porcentaje de aprobados: porcentaje_aprob")
    #If it is the same as Thursday, you will be asked for the percentage of class attendance.
    elif exam_day == "jueves": 
     asistencia = print("Ingrese el porcetaje de asistencia a clases: ")
    if asistencia > 50:
            print("Asistio la mayoria")
    else:
            print("No asistio la mayoria")
    #If the day is equal to Friday, the total income will be calculated
    if exam_day == "viernes":
      print("Comienzo del nuevo ciclo")
    cant_alumnos = int(print("Ingrese la cantidad de alumnos"))
    arancel = int(print("Ingrese el arancel por cada aluumno"))
    total = cant_alumnos * arancel
    print("El ingreso total es de ",total,"$")
else: 
 print("Error: Los datos ingresados no son válidos.")












