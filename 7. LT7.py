class Library:
    def __init__(self, listofBooks):
        self.availableBooks = listofBooks
        self.issuedBooks = {}

    def displayAvailableBooks(self):
        print("Available Books:")
        for book in self.availableBooks:
            print(book)

    def borrowBook(self, name, bookname):
        if bookname in self.availableBooks:
            self.issuedBooks[bookname] = name
            self.availableBooks.remove(bookname)
            print(f"The book '{bookname}' has been borrowed by {name}")
        else:
            print("Sorry, the book is not available in our list.")

    def returnBook(self, bookname):
        if bookname in self.issuedBooks:
            self.availableBooks.append(bookname)
            self.issuedBooks.pop(bookname)
            print(f"The book '{bookname}' has been returned.")
        else:
            print("Sorry, the book was not borrowed from here.")

    def donateBook(self, bookname):
        self.availableBooks.append(bookname)
        print(f"The book '{bookname}' has been added to the library.")

class Student:
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the book you want to return: ")
        return self.book

    def donateBook(self):
        self.book = input("Enter the name of the book you want to donate: ")
        return self.book

def main():
    IIITlibrary = Library(['Python', 'Java', 'C++', 'JavaScript'])
    student = Student()
    while True:
        print("\n1. Display all available books")
        print("2. Request for a book")
        print("3. Return a book")
        print("4. Donate a book")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            IIITlibrary.displayAvailableBooks()
        elif choice == 2:
            IIITlibrary.borrowBook(student.requestBook())
        elif choice == 3:
            IIITlibrary.returnBook(student.returnBook())
        elif choice == 4:
            IIITlibrary.donateBook(student.donateBook())
        elif choice == 5:
            break

if __name__ == "__main__":
    main()
