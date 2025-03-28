# Author: Damian Zukowski

class Property:
    def __init__(self):
        self._size = ""
        self._price = ""
        self._info = ""
        self._num_bedrooms = ""
        self._num_bathrooms = ""

    def display(self):
        print(f"Size: {self._size} Price: {self._price} Bedrooms: {self._num_bedrooms}, Bathrooms: {self._num_bathrooms} Info: {self._info}")

    def prompt_init(self):
        self._size = input("Q1. Size of the property: ")
        self._price = input("Q2. Price of the property: ")
        self._num_bedrooms = input("Q3. Number of bedrooms: ")
        self._num_bathrooms = input("Q4. Number of bathrooms: ")
        self._info = input("Q5. Provide information about the property: ")
        return self._size, self._price, self._num_bedrooms, self._num_bathrooms, self._info


# Part 2:  
class Apartment(Property):
    def __init__(self):
        super().__init__()      # Overridden method
        self._balcony = ""
        self._floor = ""

    def display(self):
        super().display()       # Overridden method
        print(f"Balcony: {self._balcony} Floor: {self._floor}")

    def prompt_init(self):
        super().prompt_init()
        self._balcony = input("Q6. Is there a balcony: ")
        self._floor = input("Q7. Which floor: ")
        return self._balcony, self._floor


# Part 3:
class House(Property):
    def __init__(self):
        super().__init__()
        self._garden_size = ""
        self._yard_size = ""
        self._garage = ""

    def display(self):
        super().display()
        print(f"Garden size: {self._garden_size} Yard size: {self._yard_size} Garage: {self._garage}")

    def prompt_init(self):
        super().prompt_init()
        self._garden_size = input("Q6. Size of the house: ")
        self._yard_size = input("Q7. Price of the house: ")
        self._garage = input("Q8. Price of the house: ")
        return self._garden_size, self._yard_size, self._garage
    

# Part 4:
class Purchase:
    def __init__(self, purchase, taxes):
        self._purchase = purchase
        self._taxes = taxes

class Rental:
    def __init__(self, rent, utilities, furnished):
        self._rent = rent
        self._utilities = utilities
        self._furnished = furnished

