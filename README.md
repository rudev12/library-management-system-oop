# Library Management System

## Overview

A simple Library Management System built using Python and Object-Oriented Programming (OOP) concepts.

This project allows librarians to manage books using unique Book IDs. The system supports adding, searching, removing, borrowing, and returning books.

## Features

* Add books to the library
* Search books using Book ID
* Remove books using Book ID
* Borrow books
* Return books
* Update book titles
* Display book information
* Basic input validation

## OOP Concepts Used

* Classes and Objects
* Constructors (`__init__`)
* Methods
* Encapsulation
* Dictionaries for data storage
* Object references

## Project Structure

### Library Class

Handles library operations such as:

* Add Book
* Search Book
* Remove Book
* Show Library Information

### Book Class

Handles book-related operations such as:

* Show Book Information
* Borrow Book
* Return Book
* Update Title

## Example Usage

```python
b1 = Book(101, "Python Basics", "Rudhraksh")

l1 = Library("Mumbai Library", "Mumbai")

l1.add_book(b1)

book = l1.search_book(101)
book.show_book()

l1.remove_book(101)
```

## Current Version

Version: v0.1

### Completed Features

* Add Book
* Search Book
* Remove Book
* Borrow Book
* Return Book
* Update Title

### Planned Features

* Show All Books
* Improved Validation
* Admin Controls
* File Storage
* Graphical User Interface (GUI)

## Author

Rudhraksh Shukla

Python Learning Project
