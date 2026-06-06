class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.available = True
    def show_book(self):
        print("=====Book-Info=====")
        print("Title:",self.title)
        print("Author:",self.author)
        print("Available:",self.available)
        
    def borrow_book(self):
        if self.available == True:
            print("Book Borrowed Successfully")
            self.available = False
        else:
            print("Book Already Borrowed")
            
    def return_book(self):
        if self.available == False:
            print("Book Returned Successfully")
            self.available = True
        else:
            print("Book Was Not Borrowed")
        
b1 = Book("Python Basics", "Rudhraksh")

b1.show_book()

b1.borrow_book()
b1.borrow_book()

b1.return_book()

b1.show_book()
