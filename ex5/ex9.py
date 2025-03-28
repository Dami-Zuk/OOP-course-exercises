# Author: Damian Zukowski

class LibraryItem:
    def __init__(self, id, title, author, publisher, year, stock):
        self._id = id
        self._title = title
        self._author = author
        self._publisher = publisher
        self._year = year
        self._stock = stock

    def display_info(self):
        return f"ID: {self._id}, Title: {self._title}, Author: {self._author}, '\n'Publisher: {self._publisher}, Year: {self._year}, Stock: {self._stock}"

    def borrow_item(self, title):
        if title:
            if self._stock > 0:
                self._stock -= 1
            else:
                print("No {title} in stock.")
        else:
            print("The {title} doesn't exist in the library.")
        return

    def return_item(self, title):
        pass
        # return the item; use title as reference and increase the stock by 1


class LibraryCatalog(LibraryItem):
    # Will hold all the LibraryItems; inheritence of LibraryItem methods + overriding + own methods

    def add_item(self, *args):
        pass
    # Takes arguments to fill the attributes;

    def remove_item(self, *args):
        pass
    # Takes args to remove the item completely - an object possibly

    def search_item(self, *args):
        pass
    # Searches for the item inside the catalog
        

class Book(LibraryItem):
    def __init__(self, id, title, author, publisher, year, stock, no_of_pages):
        super().__init__(id, title, author, publisher, year, stock)
        self._no_of_pages = no_of_pages

    