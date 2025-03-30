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

class Dice:
    def __init__(self):
        self._prev_rolls = []

    def __str__(self):
        return f"Your last roll: {self._prev_rolls[-1]}"

    def roll(self):
        value = random.randint(1,6)
        self._prev_rolls.append(value)
        return value
    
    