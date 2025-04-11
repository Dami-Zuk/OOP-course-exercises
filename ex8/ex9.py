
"""
Refactor the code, in the exercise sheet there is a list of possible problems that you can find from this program. 
Some of the problems are overlapping, so you might fix two problems when you are fixing the code.

Hint. start by utilizing inheritance and method overriding, then continue with other parts of the code.
"""

# 1. Replaced Item god-class with proper subclasses; removed None defaults; removed getters; changed methods
class Item:
    def __init__(self, title: str, year: int):
        self._title = title
        self._year = year

    # Print the description of the item
    def print_item_description(self):
        return f"Title: {self._title}, Year: {self._year}"

    # Updates the information of the item
    def update_info(self, title, year):
        if title:
            self._title = title
        if year:
            self._year = year
        else:
            return "Please provide a title and/or a year to be updated!"
 

# 2. Subclasses with overriden constructors and methods
class Book(Item):
    def __init__(self, author: str, *args):
        super().__init__(*args)
        self._author = author

    # Prints description of a Book
    def print_item_description(self):
        return f"{super().print_item_description()}, Author: {self._author}"
    
    # Updates information of the Book
    def update_info(self, author, *args):
        super().update_info(*args)
        if author:
            self._author = author
        else:
            return "Please provide the author to be updated!"


class Music(Item):
    def __init__(self, artist: str, *args):
        super().__init__(*args)
        self._artist = artist

    # Prints description of a Music
    def print_item_description(self):
        return f"{super().print_item_description()}, Artist: {self._artist}"
    
    # Updates information of the Music
    def update_info(self, artist, *args):
        super().update_info(*args)
        if artist:
            self._artist = artist
        else:
            return "Please provide the artist to be updated!"


class Movie(Item):
    def __init__(self, director: str, *args):
        super().__init__(*args)
        self._director = director

        # Prints description of a Movie
    def print_item_description(self):
        return f"{super().print_item_description()}, Director: {self._director}"
    
    # Updates information of the Movie
    def update_info(self, director, *args):
        super().update_info(*args)
        if director:
            self._director = director
        else:
            return "Please provide the director to be updated!"

class ComputerGame(Item):
    def __init__(self, developer: str, *args):
        super().__init__(*args)
        self._developer = developer

    # Prints description of a ComputerGame
    def print_item_description(self):
        return f"{super().print_item_description()}, Developer: {self._developer}"
    
    # Updates information of the ComputerGame
    def update_info(self, developer, *args):
        super().update_info(*args)
        if developer:
            self._developer = developer
        else:
            return "Please provide the developer to be updated!"


# 3. Added encapsulation for each class
class Box:
    def __init__(self):
        self._items = {}

    # Adds the item to the dictionary
    def add_item(self, key, item: Item):
        self._items[key] = item

    # Removes the item from the dictionary
    def remove_item(self, key):
        if key in self._items:
            del self._items[key]
        else:
            return "No item found with the given name."

    # Replaces the item in the dictionary
    def replace_item(self, old_key, new_key, new_item):
        if old_key in self._items:
            del self._items[old_key]
            self._items[new_key] = new_item
        else:
            print("No item found to be replaced.")

    # Returns a list of items descriptions
    def get_descriptions(self):
        return [item.print_item_description() for item in self._items.values()]
    
# 4. Used **kwargs to apply all the item parameters
    # Updates the item in the dictionary
    def update_item(self, key, **kwargs):
        # Hint! check here how to use kwarks!
        # for example: https://realpython.com/python-kwargs-and-args/   ** unpacks dictionaries
        if key in self._items:
            self._items[key].update_info(**kwargs)
        else:
            print("No item found with the given name.")

class PackItems:
    def __init__(self):
        self._box = Box()
        self._log = []

    def user_interface(self):
        while True:
            print("\nOptions:")
            print("1. Add item")
            print("2. Remove item")
            print("3. Replace item")
            print("4. View items")
            print("5. Update item")
            print("6. Exit")
            choice = input("Choose an option: ")

# 4. Replaced unneccessary inputs with function calls from Box class; added missing choice nr 4;
            if choice == "1":
                key = input("Item name to be added: ")
                item = self.build_item_from_inputs()
                self._box.add_item(key, item)
                self._log.append(f"Added item: {key}")

            elif choice == "2":
                key = input("Item name to be removed: ")
                self._box.remove_item(key)
                self._log.append(f"Removed item: {key}")

            elif choice == "3":
                old_key = input("Item name to be replaced: ")
                new_key = input("New item name: ")
                new_item = self.build_item_from_inputs()
                self._box.replace_item(old_key, new_key, new_item)
                self._log.append(f"Replaced item: {old_key}")

            elif choice == "4":
                for item in self._box.get_descriptions():
                    print(item)

            elif choice == "5":
                key = input("Item name to be updated: ")
                # self._box.update_item()
                # self._log.append(f"Removed item: {key}")

            elif choice == "6":
                self.save_log()
                break
            else:
                print("Invalid option. Please try again.")

    def save_log(self):
        with open("log.txt", "w") as file:
            for entry in self._log:
                file.write(entry + "\n")
      
    # 5. Added necessary item builder method
    def build_item_from_inputs(self):
        print("Select item type (enter a number): ")
        choice = input("1 - Book, 2 - Music, 3 - Movie, 4 - Computer Game: ")
        title = input("Enter title: ")
        year = input("Enter year: ")

        if choice == "1":
            author = input("Enter author: ")
            return Book(author, title, year)
        elif choice == "2":
            artist = input("Enter artist: ")
            return Music(artist, title, year)
        elif choice == "3":
            director = input("Enter director: ")
            return Movie(director, title, year)
        elif choice == "4":
            developer = input("Enter developer: ")
            return ComputerGame(developer, title, year)
        else:
            print("Wrong item type!")


# Example usage:

# This is for testing the Item subclasses
"""
if __name__ == "__main__":
    item1 = Book("1984", "George Orwell", 1949)
    item2 = Music("Thriller", "Michael Jackson", 1982)
    item3 = Movie("Inception", "Christopher Nolan", 2010)
    item4 = ComputerGame("The Legend of Zelda", "Nintendo", 1986)

    print(item1.print_item_description())
    print(item2.print_item_description())
    print(item3.print_item_description())
    print(item4.print_item_description())"""


# This is for testing the Box class
"""
if __name__ == "__main__":
    box = Box()
    box.add_item("1984", Book("1984", "George Orwell", 1949))
    box.add_item("Thriller", Movie("Thriller", "Michael Jackson", 1982))

    print("Before replacement:")
    for description in box.get_descriptions():
        print(description)

    box.replace_item("1984", "1984", Book("1984", "George Orwell", 1950))

    print("\nAfter replacement:")
    for description in box.get_descriptions():
        print(description)
"""


if __name__ == "__main__":
    pack_items = PackItems()
    pack_items.user_interface()



