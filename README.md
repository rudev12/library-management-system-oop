# Library Management System

## Overview

A Library Management System built using Python and Object-Oriented Programming (OOP) concepts.

This project allows users to manage books in a library by adding, searching, borrowing, returning, updating, and removing books. It also provides library statistics and multiple search options.

---

## Features

### Library Features

* Add Book
* Search Book by ID
* Remove Book
* Show All Books
* Library Statistics
* Search Books by Title
* Search Books by Author
* Check Book Availability
* Count Books by Author

### Book Features

* Show Book Details
* Borrow Book
* Return Book
* Update Book Title

---

## OOP Concepts Used

* Classes and Objects
* Constructors (`__init__`)
* Methods
* Dictionaries
* Encapsulation
* Object Composition
* Conditional Statements
* Loops

---

## Classes

### Library Class

Methods:

* `show_library()`
* `add_book()`
* `search_book()`
* `remove_book()`
* `show_all_books()`
* `library_stats()`
* `search_by_title()`
* `search_by_author()`
* `check_availability()`
* `count_book_by_author()`

### Book Class

Methods:

* `show_book()`
* `borrow_book()`
* `return_book()`
* `update_title()`

---

## Example Usage

```python
b1 = Book(101, "Python Basics", "Rudhraksh")
b2 = Book(102, "C++ Basics", "Swayam")

l1 = Library("Mumbai Library", "Mumbai")

l1.add_book(b1)
l1.add_book(b2)

count = l1.count_book_by_author("Swayam")
print("Total Books:", count)

l1.check_availability(101)

result = l1.search_by_title("Python Basics")

for book in result:
    book.show_book()
```

---

## Current Version

Version: 0.5

Completed Features

1. Add Book
2. Search Book by ID
3. Remove Book
4. Show All Books
5. Library Statistics
6. Borrow Book
7. Return Book
8. Update Title
9. Search by Title
10. Search by Author
11. Check Availability
12. Count Books by Author

---

## Future Improvements

* Update Author
* Search by Partial Title
* Search by Partial Author
* Employee Management
* Fine Management System
* Issue Date Tracking
* Return Date Tracking
* File Handling
* JSON Data Storage
* SQLite Database Integration
* Login System
* GUI Version Using Tkinter
* Web Version Using Flask or Django

---

## Author

Rudhraksh Shukla

Python OOP Learning Project
