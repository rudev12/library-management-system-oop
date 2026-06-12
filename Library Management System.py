class Library:
    def __init__(self, library_name, address):
        self.library_name = library_name
        self.address = address
        self.books = {}
        self.number_employees = 0

    def show_library(self):
        print("Name of library:",self.library_name)
        print("Address:",self.address)
        print("Total Books:",len(self.books))
        print("Total Employee Working:", self.number_employees)
        
    def add_book(self,book):
        self.books[book.book_id] = book
        print("Book Added Successfully")
        
    def search_book(self,book_id):
        if book_id == "   ":
            print("Book Id Cannot be Empty")
        elif book_id not in self.books:
            print("Book Id Not Exists Please Enter Valid Id")
        else:
            return self.books[book_id]
            
    def remove_book(self,book_id):
        if book_id == "   ":
            print("Book Id Cannot be Empty")
        elif book_id not in self.books:
            print("Book Id Not Exists Please Enter Valid Id")
        else:
            book =self.books[book_id]
            del self.books[book_id]
            print("Book Removed Sucessfully")
            return book

class Book:
    def __init__(self,book_id,title,author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True
    def show_book(self):
        print("=====Book-Info=====")
        print("Book Id:",self.book_id)
        print("Title:",self.title)
        print("Author:",self.author)
        print("Available:",self.available)
        
    def borrow_book(self):
        if self.available :
            print("Book Borrowed Successfully")
            self.available = False
        else:
            print("Book Already Borrowed")
            
    def return_book(self):
        if not self.available:
            print("Book Returned Successfully")
            self.available = True
        else:
            print("Book Was Not Borrowed")
    
    def update_title(self, new_title):
        if new_title == " ":
            print("Title Cannot Be Empty")
        else:
            self.title = new_title
            print("Title Updated Successfully")
            print("Title:",self.title)
        
b1 = Book(101,"Python Basics", "Rudhraksh")
b2 = Book(102,"C++ Basics ","Swayam")
l1 = Library("Mumbai Library", "Mumbai")
l1.add_book(b1)
l1.add_book(b2)
book = l1.remove_book(101)
book.show_book()
b2.show_book()
