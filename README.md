# Library Management System

## Overview

A Library Management System built using Python and Object-Oriented Programming (OOP) concepts.

This project allows users to manage books in a library using unique Book IDs. The system supports adding, searching, removing, borrowing, returning, and updating books while maintaining library statistics.

---

## Features

### Library Features

* Add books to the library
* Search books by Book ID
* Remove books from the library
* Show all books in the library
* Display library statistics

### Book Features

* Display book information
* Borrow a book
* Return a book
* Update book title

---

## OOP Concepts Used

* Classes and Objects
* Constructors (`__init__`)
* Methods
* Encapsulation
* Object References
* Dictionary-based Data Storage

---

## Project Structure

### Library Class

Responsible for managing the library.

Methods:

* `show_library()`
* `add_book()`
* `search_book()`
* `remove_book()`
* `show_all_books()`
* `library_stats()`

### Book Class

Responsible for managing book information.

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

l1.show_all_books()

l1.library_stats()
```

---

## Sample Output

```text
Total Books: 2
Total Available Books: 2
Total Borrowed Books: 0
```

---

## Current Version

### Version: v0.2

Completed Features:

* Add Book
* Search Book
* Remove Book
* Show All Books
* Library Statistics
* Borrow Book
* Return Book
* Update Title

---

## Upcoming Features

* Search Book by Title
* Search Book by Author
* Employee Management
* Librarian Management
* File Storage
* Database Integration
* GUI Interface

---

## Author

Rudhraksh Shukla

Python OOP Learning Project
