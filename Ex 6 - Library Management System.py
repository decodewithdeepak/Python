class Library:
    def __init__(self):
        self.noOfBooks = 0
        self.books = []

    def addBook(self, book):
        self.books.append(book)
        self.noOfBooks = len(self.books)

    def showInfo(self):
        print(f"The library has {self.noOfBooks} books.\nThe books are :")
        for book in self.books:
            print(book)


l1 = Library()
l1.addBook("Harry Potter1")
l1.addBook("Harry Potter2")
l1.addBook("Harry Potter3")
l1.addBook("Harry Potter4")
l1.addBook("Harry Potter5")

l1.showInfo()

