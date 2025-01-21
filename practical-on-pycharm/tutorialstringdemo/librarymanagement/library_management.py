class Book:
    def __init__(self, name, author, isbn):
        self.name=name
        self.author=author
        self.isbn=isbn
    def display_info(self):
        print(f"name: {self.name}, author: {self.author}, isbn: {self.isbn}")

class Library:
    def __init__(self):
        self.books=[]
    def add_book(self,book):
        self.books.append(book)
        print(f"Book {book.name} added to the library")
    def remove_book(self,isbn):
        book_to_remove=None
        for book in self.books:
            if book.isbn==isbn:
                book_to_remove=book
        # check if book is there then remove
        if book_to_remove:
            self.books.remove(book_to_remove)
            print(f"book {book_to_remove.name} removed from the library")
    def display_books(self):
        #If no book in the list
        if not self.books:
            print("No books in the library")
        else:
            for book in self.books:
                book.display_info()

#Inheritace- SpecialLibrary uses functionality of Library
#Overriding- add_book() of Library override in SpecialLibrary
#Polymorphism- Overriding is a runtime polymorphism
class SpecialLibrary(Library):
    def add_book(self,book):
        super().add_book(book)
        print(f"Special handling for book {book.name}")

book1 = Book("Azure OpenAI","Shila Kumari","123")
book2 = Book("AWS Lambda","Shila Kumari","456")

lib1=Library()
#add books to the library
lib1.add_book(book1)
lib1.add_book(book2)
lib1.display_books()

#remove books from the library
lib1.remove_book("123")
lib1.display_books()

special_library=SpecialLibrary()
special_library.add_book(book1)

lib1.display_books()
