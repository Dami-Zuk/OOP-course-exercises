# Author: Damian Zukowski

# SECRET MAGIC POTION:
class MagicPotion:
    def __init__(self, name: str):
        self._name = name
        self._ingredients = []

    def add_ingredient(self, ingredient: str, amount: float):
        self._ingredients.append((ingredient, amount))

    def print_recipe(self):
        print(self._name + ":")
        for ingredient in self._ingredients:
            print(f"{ingredient[0]} {ingredient[1]} grams")

""" Please define a class named SecretMagicPotion which inherits the MagicPotion class and allows
you to also protect the recipe with a password.
The new class should have a constructor which also takes the password string as an argument.
The class should also contain the following methods:
• add_ingredient(ingredient: str, amount: float, password: str)
• print_recipe(password: str)
If the password argument given to either of these methods is wrong, the methods should raise a
ValueError exception. 
If the password is correct, each method should call the relevant method in the parent class. Do not
copy and paste anything from the MagicPotion class."""

class SecretMagicPotion(MagicPotion):
    def __init__(self, name, password):
        super().__init__(name)
        self.__password = password

    def add_ingredient(self, ingredient: str, amount: float, password: str):
        if password == self.__password:
            super().add_ingredient(ingredient, amount)
        else:
            raise ValueError("Wrong password!")

    def print_recipe(self, password:str):
        if password == self.__password:
            super().print_recipe()
        else:
            raise ValueError("Wrong password!")


# Test prints
diminuendo = SecretMagicPotion("Diminuendo maximus", "hocuspocus")
diminuendo.add_ingredient("Toadstool", 1.5, "hocuspocus")
diminuendo.add_ingredient("Magic sand", 3.0, "hocuspocus")
diminuendo.add_ingredient("Frogspawn", 4.0, "hocuspocus")
diminuendo.print_recipe("hocuspocus")
diminuendo.print_recipe("pocushocus") # WRONG password!
