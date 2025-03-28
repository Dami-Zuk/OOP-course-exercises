# Author: Damian Zukowski

class LunchCard:
    def __init__(self, balance:float):
        self.balance = balance

    # Part 1: String representation of the object, rounds the balance to 1 decimal point.
    def __str__(self):
        return f"Your balance is { round(float(self.balance), 1) } euros."
    
    # Part 2: Deducts 2.95 from the card balance, checks for enough funds.
    def eat_ordinary(self):
        if self.balance >= 2.95:
            self.balance -= 2.95
        else:
            raise ValueError("Insufficient funds!")
        
    # Part 2: Deducts 5.9 from the card balance, checks for enough funds.
    def eat_luxury(self):
        if self.balance >= 5.9:
            self.balance -= 5.9
        else:
            raise ValueError("Insufficient funds!")
        
    # Part 3: Adds money to the card, checks if correct input.
    def deposit_money(self, funds:float):
        try:
            funds = float(funds)
            if funds > 0:
                self.balance += funds
            else:
                return "Deposit must be a positive number!"
        except ValueError:
            return "Wrong amount - must be a number!"
        

# Part 4: main function with sequence of events
def main():
    peter = LunchCard(20)
    grace = LunchCard(30)

    peter.eat_luxury()
    grace.eat_ordinary()
    print("Peter: ", peter, "\nGrace: ", grace)

    peter.deposit_money(20)
    grace.eat_luxury()
    print("Peter: ", peter, "\nGrace: ", grace)

    peter.eat_ordinary()
    peter.eat_ordinary()

    grace.deposit_money(50)
    print("Peter: ", peter, "\nGrace: ", grace)
    

# Test objects and prints
main()

""" card1 = LunchCard(50)
card2 = LunchCard(2)
print(card1, card2)

card1.eat_luxury()
# card2.eat_ordinary()
print(card1)

card2.deposit_money(10)
print(card2)"""


