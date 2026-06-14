# 📚 Library Management System

## Overview

A Python-based Library Management System built using Object-Oriented Programming (OOP) concepts.

This project allows users to manage books inside a library by adding, searching, borrowing, returning, updating, and removing books while also generating library statistics.

---

# Features

## Library Features

### Add Book

Add a new book to the library.

### Search Book by ID

Search and retrieve a book using its unique Book ID.

### Remove Book

Remove a book from the library collection.

### Show All Books

Display all books currently available in the library.

### Library Statistics

Display:

* Total Books
* Available Books
* Borrowed Books

### Search by Title

Search books using their title.

### Search by Author

Search books written by a specific author.

---

## Book Features

### Show Book Details

Display complete information about a book.

### Borrow Book

Mark a book as borrowed.

### Return Book

Mark a borrowed book as returned.

### Update Title

Update the title of a book.

---

# OOP Concepts Used

* Classes and Objects
* Constructors (`__init__`)
* Methods
* Object References
* Dictionaries
* Encapsulation
* Composition

---

# Project Structure

## Library Class

Methods:

* `show_library()`
* `add_book()`
* `search_book()`
* `remove_book()`
* `show_all_books()`
* `library_stats()`
* `search_by_title()`
* `search_by_author()`

---

## Book Class

Methods:

* `show_book()`
* `borrow_book()`
* `return_book()`
* `update_title()`

---

# Example Usage

```python
b1 = Book(101, "Python Basics", "Rudhraksh")
b2 = Book(102, "C++ Basics", "Swayam")

l1 = Library("Mumbai Library", "Mumbai")

l1.add_book(b1)
l1.add_book(b2)

b2.borrow_book()

l1.library_stats()

result = l1.search_by_title("Python Basics")

for book in result:
    book.show_book()

final = l1.search_by_author("Swayam")

for book in final:
    book.show_book()
```

---

# Current Version

## Version 0.3

Completed Features:

* Add Book
* Search Book by ID
* Remove Book
* Show All Books
* Library Statistics
* Borrow Book
* Return Book
* Update Title
* Search by Title
* Search by Author

---

# Future Improvements

* Employee Management
* Librarian Management
* Fine Management System
* Issue Date & Return Date Tracking
* File Handling (Save Data)
* JSON Storage
* Database Integration (SQLite/MySQL)
* Login System
* GUI Version using Tkinter
* Web Version using Flask/Django

---

# Author

**Rudhraksh Shukla**

Python OOP Learning Project
