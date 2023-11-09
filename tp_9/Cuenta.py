class Account:
    def __init__(self, holder, balance=0.0):
        self.__holder = holder
        self.__balance = balance

    # Getters
    def get_holder(self):
        return self.__holder

    def get_balance(self):
        return self.__balance

    # Method to display account details
    def display(self):
        print(f"titular: {self.__holder}")
        print(f"Cantidad: {self.__balance:.2f}")

    # Method to deposit money into the account
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    
     # Method to withdraw money from the account
    def withdraw(self, amount):
        if amount > 0:
            self.__balance -= amount
# Example of usage


Account_1 = Account("Ignacio", 1000.0)

Account_1.display()
print("-------------------")
Account_1.deposit(500.0)
Account_1.display()

print("-------------------")
Account_1.withdraw(200.0)
Account_1.display()

