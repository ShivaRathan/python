import json

class Book:
    def __init__(self, title, author, year, isbn):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
    
    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "isbn": self.isbn
        }

class Library:
    def __init__(self, filename):
        self.filename = filename
        self.books = []
        self.load_books()
    
    def load_books(self):
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                self.books = [Book(**book) for book in data]
        except FileNotFoundError:
            print("No previous data found. Starting with an empty library.")
        except json.JSONDecodeError:
            print("Error decoding the data. Starting with an empty library.")
    
    def save_books(self):
        with open(self.filename, 'w') as file:
            json.dump([book.to_dict() for book in self.books], file, indent=4)
    
    def add_book(self, book):
        self.books.append(book)
        self.save_books()
    
    def remove_book(self, isbn):
        self.books = [book for book in self.books if book.isbn != isbn]
        self.save_books()
    
    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def list_books(self):
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}, Year: {book.year}, ISBN: {book.isbn}")

def main():
    library = Library('library_data.json')

    while True:
        print("\nLibrary Menu:")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Find Book")
        print("4. List Books")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            year = int(input("Enter book year: "))
            isbn = input("Enter book ISBN: ")
            book = Book(title, author, year, isbn)
            library.add_book(book)
        elif choice == '2':
            isbn = input("Enter ISBN of the book to remove: ")
            library.remove_book(isbn)
        elif choice == '3':
            isbn = input("Enter ISBN of the book to find: ")
            book = library.find_book(isbn)
            if book:
                print(f"Found Book - Title: {book.title}, Author: {book.author}, Year: {book.year}, ISBN: {book.isbn}")
            else:
                print("Book not found.")
        elif choice == '4':
            library.list_books()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
