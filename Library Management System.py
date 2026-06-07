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
        
b1 = Book(101,"Python Basics", "Rudhraksh")

b1.show_book()

b1.borrow_book()
b1.borrow_book()

b1.return_book()

b1.show_book()
