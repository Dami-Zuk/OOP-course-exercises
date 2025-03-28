# Author: Damian Zukowski

class FavBook():

    def __init__(self, title, author, genre, year, rating):
        self.title = title
        self.author = author
        self.genre = genre
        self.year = year
        self.rating = rating

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Genre: {self.genre}, Year: {self.year}, Rating: {self.rating}"
    

my_book_1 = FavBook("The Way of Kings", "Brandon Sanderson", "fantasy", "2010", "AMAZING")
my_book_2 = FavBook("The Lord of the Ice Garden", "Jaroslaw Grzedowicz", "fantasy", "2007", "Great")

print(f"The title of my first fav book is {my_book_1.title} by {my_book_1.author}.")
print(my_book_2)
