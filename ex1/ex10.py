# Author: Damian Zukowski

# Task 10

phonebook = {}

def searchItems(name):
    if name in phonebook:
        print("Number: ", phonebook[name])
    else:
        print("No number!")
    return


def addItem():
    name = input("Enter a name: ")
    number = input("Enter a number: ")
    phonebook[name] = number
    print("Ok!")
    return 


def ex10():
    while True:
        try:
            choice = int(input("Enter a command: 1 - search, 2 - add, 3 - quit: "))
        except ValueError:
            pass
            

        if choice == 1:
            name = input("Enter a name to find: ")
            searchItems(name)
        elif choice == 2:
            addItem()
        elif choice == 3:
            print("Closing the phonebook.")
            break
        else:
            print("Wrong input! Enter 1, 2 or 3.")


ex10()
