# Author: Damian Zukowski

# Task 8
import random

def computer_choice():
    choice = random.randint(1, 3)
    if choice == 1:
        return "rock"
    elif choice == 2:
        return "paper"
    else:
        return "scissors"

def user_choice():
    choice = input("Enter your choice -> rock, paper or scissors: ")
    return choice

def ex8():
    user = user_choice()
    computer = computer_choice()
    print("Computer choice: ", computer)

    if user == computer:
        return "DRAW!"
    elif user == "rock" and computer == "scissors" or user == "paper" and computer == "rock" or user == "scissors" and computer == "paper":
        return "USER WINS"
    else:
        return "COMPUTER WINS"

print("Results: ", ex8())
