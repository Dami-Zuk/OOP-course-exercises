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


book_1 = FavBook("The Way of Kings", "Brandon Sanderson", "fantasy", "2010", "AMAZING")
book_2 = FavBook("The Lord of the Ice Garden", "Jaroslaw Grzedowicz", "fantasy", "2007", "Great")
book_3 = FavBook("Dune", "Frank Herbert", "sci-fi", "1966", "Lisan al-gaib!")
book_4 = FavBook("Metro 2033", "Dmitry Glukhovsky", "post-apo", "2002", "Love it")

books = [book_1, book_2, book_3, book_4]    # list of 4 books of type FavBook

def books_of_genre(books: list, genre: str):
    matching_books = []
    for item in books:
        if item.genre == genre:
            matching_books.append() # simple print
        else:
            pass

    if matching_books:
        return matching_books
    else:
        return f"No books found with genre {genre}."
        

print("Books found with chosen genre: ", books_of_genre(books, "post-apo"))