# Author: Damian Zukowski

class Pet():

    def __init__(self, name, species, year_of_birth):
        self.name = name
        self.species = species
        self.year_of_birth = year_of_birth

    def __str__(self):
        return f"Name: {self.name}, Species: {self.species}, Year of birth: {self.year_of_birth}"
    

def new_pet(name: str, species: str, year_of_birth: str):
    new_pet = Pet(name, species, year_of_birth)
    return new_pet

my_pet = new_pet("Leon", "domestic long-hair", "2017")
print(my_pet.name)
print(my_pet)
