# Author: Damian Zukowski

# Part 1
class Item:
    def __init__(self, name: str, weight: int):
        self.__name = name
        self.__weight = weight

    def name(self):
        return self.__name
    
    def weight(self):
        return self.__weight
    
    def __str__(self):
        return f"{self.__name} {self.__weight}g"

"""
book = Item("ABC Book", 200)
phone = Item("Nokia 3210", 100)

print("Name of the book:", book.name())
print("Weight of the book:", book.weight())
print("Book:", book)
print("Phone:", phone) """


# Part 2
class Suitcase:
    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__items = []
        self.__weight_counter = 0

    # Adds an item to the suitcase; checks if the item is not too heavy or crosses the max weight limit
    def add_item(self, item):
        if self.__weight_counter + item.weight() <= self.__max_weight:
            self.__items.append(item)
            self.__weight_counter += item.weight()

    # Part 3: modified method to return singular "item" string if only 1 item in the suitcase.
    def __str__(self):
        if len(self.__items) == 1:
            return f"{len(self.__items)} item ({self.__weight_counter} g)"
        else:
            return f"{len(self.__items)} items ({self.__weight_counter} g)"
        
    # Part 4: Prints all items in the suitcase; iterates through the items list to call Item __str__ method
    def print_items(self):
        # print("All items in the suitcase:")
        for item in self.__items:
            print(item)     # calls __str__ method from Item

    def weight(self):
        return self.__weight_counter
    
    # Part 5: Assumes 1st item is heaviest; checks if there are heavier ones.
    def heaviest_item(self):
        if self.__items:
            heaviest = self.__items[0]
            for item in self.__items:
                if item.weight() > heaviest.weight():
                    heaviest = item
            return str(heaviest)
        else:
            return None
        

# Test prints
book = Item("ABC Book", 200)
phone = Item("Nokia 3210", 100)
brick = Item("Brick", 400)
suitcase = Suitcase(500)

print(suitcase)
suitcase.add_item(book)
print(suitcase)
suitcase.add_item(phone)
print(suitcase)
suitcase.add_item(brick)
print(suitcase)

print("PART 4")
suitcase.print_items()
print(f"Combined weight: {suitcase.weight()} g")

print("PART 5")
suitcase2 = Suitcase(1000)
suitcase2.add_item(book)
suitcase2.add_item(phone)
suitcase2.add_item(brick)
heaviest = suitcase2.heaviest_item()
print(f"The heaviest item: {heaviest}")


# Part 6:
class CargoHold:
    def __init__(self, max_weight):
        self.__max_weight = max_weight * 1000   # Kilograms to grams
        self.__weight_counter = 0
        self.__cargo = []

    # Adds suitcase to the cargo list; checks if max weight is crossed
    def add_suitcase(self, suitcase):
        if self.__weight_counter + suitcase.weight() <= self.__max_weight:
            self.__cargo.append(suitcase)
            self.__weight_counter += suitcase.weight()

    def weight(self):
        return self.__weight_counter

    def __str__(self):
        space_kg = (self.__max_weight - self.__weight_counter) / 1000   # Grams to kilograms
        return f"{len(self.__cargo)} suitcases, space for {space_kg} kg"
    
    # Part 7
    def print_items(self):
        for item in self.__cargo:
            item.print_items()


print("PART 6")
cargo_hold = CargoHold(100)
print(cargo_hold)

book = Item("ABC Book", 200)
phone = Item("Nokia 3210", 100)
brick = Item("Brick", 400)

adas_suitcase = Suitcase(1000)
adas_suitcase.add_item(book)
adas_suitcase.add_item(phone)
peters_suitcase = Suitcase(1000)
peters_suitcase.add_item(brick)

cargo_hold.add_suitcase(adas_suitcase)
print(cargo_hold)
cargo_hold.add_suitcase(peters_suitcase)
print(cargo_hold)

print("PART 7")
print("The suitcases in the cargo hold contain the following items:")
cargo_hold.print_items()

