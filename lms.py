class Library:
    def __init__(self):
        file = "books.txt"
        self.file = file
        self.file = open(self.file, "a+")
        
    def list_books(self):
        file = open("books.txt", "r")
        print(file.read().splitlines())
        
    def add_book(self, book):
        file = open("books.txt", "a+")
        file.write(book)
        
    def remove_book(self, title):
        
        with open("books.txt", "r") as file:
            lines = file.readlines()
    
        with open("books.txt", "w") as file:
            for line in lines:
                if title.lower() not in line.lower().split(', ')[0]:
                    file.write(line)


lib = Library()

while True:
    sec = input("\n  MENU\n-------\n 1) List Books\n 2) Add Book\n 3) Remove Book\n q) Quit\nChoose an option:")
    
    if sec == "1":
        lib.listBooks()
        
    elif sec == "2":
        title = input("Title: ").strip().title()
        author = input("Author: ").strip().title()
        year = input("Release Date: ").strip()
        pages = input("Pages: ").strip()
        book = (f"{title}, {author}, {year}, {pages}\n")
        lib.addBook(book)
        print(f"\n{title} is added to the library.")
        
    elif sec == "3":
        title_to_remove = input("Enter the title of the book to remove: ").strip().title()
        lib.removeBook(title_to_remove)
        
    elif sec == "q":
        quit()
    else:
        print("Enter a valid command")