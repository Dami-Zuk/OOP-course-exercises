# Author: Damian Zukowski

class BankAccount:
    def __init__(self, owner:str, acc_num:str, balance:float):
        self.__owner = owner
        self.__acc_num = acc_num
        self.__balance = balance

    # Adds money to the account
    def deposit(self, amount:float):
        try:                            # Check if the amount is a float
            amount = float(amount)
            if amount > 0:              # Check if the amount is a positive number
                self.__balance += amount
                self.__service_charge()
            else:
                raise ValueError("Deposit failed. The amount must be a positive number!")
        except ValueError:
            raise ValueError("Deposit failed.")

    # Withdraws money from the account
    def withdraw(self, amount:float):
        try:                            # Check if the amount is a float
            amount = float(amount)
            if amount <= 0:             # Check if the amount is negative
                raise ValueError("Withdrawal failed. The amount must be a positive number!")
            elif self.__balance >= amount:   # Check if the balance is larger than withdrawal amount
                self.__balance -= amount
                self.__service_charge()
            else:
                raise ValueError("Insufficient funds on the account!")
        except ValueError:
            raise ValueError("Withdrawal failed.")
        
    # Balance getter
    @property
    def balance(self):
        return f"Your account balance: { self.__balance }"
    
    # Private method to deduct 1% off balance after each deposit and withdrawal operation
    def __service_charge(self):
        self.__balance *= 0.99


# Test object and prints
account = BankAccount("Randy Riches", "12345-6789", 1000)

account.withdraw(100)
print(account.balance)

account.deposit(100)
print(account.balance)

# account.deposit(-5)

