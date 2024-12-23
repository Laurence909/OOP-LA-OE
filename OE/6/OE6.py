#OE6
class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("withdraw amount must be positive")
            
    def withdraw(self, amount):
        
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            return amount
        else:
            print("withdraw amount must be positive")
            
    def display_account_info(self):
        print(f"account number: {self.__account_number}\nyour current balance is: {self.__balance}")
        
    def __display_balance(self):
        return self.__balance
        
    def get_account_number(self):
        return f"Account Number: {self.__account_number}"
        
    def get_balance(self):
        return f"Current Balance: {self.__balance}"
        
    def set_account_number(self):
        return self.__account_number
        
    def set_balance(self, balance):
        if balance > 0:
            self.__balance = balance
        else:
            print("Error balance")

account_info = BankAccount(12345, 0)
account_info.deposit(1500.00)
account_info.withdraw(1400.00)
account_info.set_balance(-500)
account_info.display_account_info()
