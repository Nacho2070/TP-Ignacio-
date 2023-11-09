class Person:
    def __init__(self, name="", age=0, dni=""):
        self.__name = name
        self.__age = age
        self.__dni = dni

    # Getters
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_dni(self):
        return self.__dni

    # Setters with validation
    def set_name(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            print("Error el nombre debe ser un str")

    def set_age(self, age):
        if isinstance(age, int) and age >= 0:
            self.__age = age
        else:
            print("La edad no puede tener numeros negativos")

    def set_dni(self, dni):
      if isinstance(dni, int):
        self.__dni = str(dni)  # Almacenar el DNI como una cadena de texto
      else:
        print("El DNI debe ser un número entero.")

    def show(self):
        print(f"Name: {self.__name}")
        print(f"Age: {self.__age}")
        print(f"DNI: {self.__dni}")

    def isAdult(self):
        return self.__age >= 18

    
# Example of usage    
    
person_1 = Person()
person_1.set_name("Ignacio Ariza")
person_1.set_age(19)
person_1.set_dni("45715658")
person_1.mostrar()