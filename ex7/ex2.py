# Author: Damian Zukowski

""" Part 1: Simple dice game
Create multiple dices (at least three) and put them in a list. See that your dice can be rolled, and the
side can be shown. Create a small game where the best sum of three rolls wins. If the sum is a tie, tied
dices are rolled until the winner is found (best side wins). Use functions and pass objects (or list of
objects) as arguments. Use informative and clear output prints.
Part 2: Add dices
Change your program now so that you can use any number of dices, e.g. number of dices. The number
of dices that is going to be used is asked from the user.
part 3: Add Players
Create a class called Player. Player has at least the following data attributes: name and a player id.
Remember to code accessor (getters) and mutator (setters) methods and str-method, use the Pythonic
way, i.e. use the property decorator.
Create a dictionary so that the player id is the key and each player has one dice. Roll each player’s dice
and print out each player’s dice’s side. Use informative and clear output prints. Create the dictionary in
main function in this exercise. If this is too difficult, start with creating 1 player. Then try to extend to
multiple players if you can.
part 4: Add Mammals
Create a mammal class. It has the following data attributes: ID, species, name, size and weight.
Part 5: Add pet to each player
Add one data attribute to player (= add it to Player class), attribute is called pet and it is always a
mammal. Add also a method that helps to set the pet to the player. In the main function, give every
player one mammal and print out each player and their mammal’s information. Use informative and
clear output print. If this is too difficult, start with 1 player and then extend to multiple players if you
can.
Part 6: Mammal based on dice game result
Let the player select their pet mammal by rolling 2 dices and using their sum to indicate a mammal (use
here the dice game that you developed at the early part of this exercise). The higher the number, the
heavier mammal you get as your pet. Remember to implement the selection logic in e.g., main function
(so not inside any class). Thus, you are of course allowed to (and supposed to) call class’s methods from
main (e.g. roll_dice, get_side etc.)"""
import random

# Part 1 - Dice and GameOfDices classes
class Dice:
    def __init__(self):
        self._prev_rolls = []

    def __str__(self):
        return f"Your last roll: {self._prev_rolls[-1]}"

    def roll(self):
        value = random.randint(1,6)
        self._prev_rolls.append(value)
        return value


class GameOfDices:
    def __init__(self, dices: list):
        self.dices = dices

    def play(self):
        print("Rolling all dices \n")
        for i in len(players):
            players[i] 
        

# Part 4 - Mammal class
class Mammal:
    def __init__(self, id: int, species: str, name: str, size: str, weight: int):
        self.__id = id
        self.__species = species
        self.__name = name
        self.__size = size
        self.__weight = weight

    # Part 5
    def __str__(self):
        return f"Name: {self.__name}, Species: {self.__species}, Size: {self.__size}, Weight: {self.__weight}kg"


# Part 3 - Player class
class Player:
    def __init__(self, name: str, player_id: int):
        self.__name = name
        self.__player_id = player_id
        self.__pet = None   # Part 5 - assigning a pet

    @property
    def name(self):
        return self.__name
    
    @property
    def player_id(self):
        return self.__player_id
    
    @name.setter
    def name(self, value):
        self.__name = value

    @player_id.setter
    def player_id(self, value):
        self.__player_id = value

    # Part 5 - assigning a pet to the player and str method
    def assign_pet(self, pet: Mammal):
        if isinstance(pet, Mammal):     # isinstance(obj, type) returns True or False
            self.__pet = pet
        else:
            raise ValueError("The pet must be of Mammal type!")

    def __str__(self):
        if self.__pet:
            pet_info = str(self.__pet)
        else:
            pet_info = "No pet assigned."

        return f"Player {self.__name} - ID: {self.__player_id} - Pet: {pet_info}"


# DICES
dice1 = Dice()
dice2 = Dice()
dice3 = Dice()
list_of_dices = [dice1, dice2, dice3]

# PLAYERS
player1 = Player("Dobby", 123)
player2 = Player("Johnny", 456)
player3 = Player("Bingus", 789)

players = {
    player1.player_id: dice1,
    player2.player_id: dice2,
    player3.player_id: dice3,
}

# PETS
monke = Mammal(1, "Gorilla", "Harambe", "BIG", 120)
doggo = Mammal(2, "Shiba Inu", "Good Boi", "Medium", 20)
catto = Mammal(3, "Abyssinian", "Hiss", "Small", 5)

# TESTS
# list_of_dices[1].roll()
# print(f"{player1.name} rolled: {players[player1.player_id].roll()}")
# print(f"{player2.name} rolled: {players[player2.player_id].roll()}")

player1.assign_pet(monke)
player2.assign_pet(doggo)
player3.assign_pet(catto)

print(player1)



