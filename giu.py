import tkinter as tk
from tkinter import ttk, messagebox, simpledialog



class Book:
    def __init__(self, book_id, title, author, available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = available

    def show_book(self):
        print("=====Book-Info=====")
        print("Book Id:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Available:", self.available)

    def update_title(self, new_title):
        self.title = new_title


class Library:
    def __init__(self, library_name, address):
        self.library_name = library_name
        self.address = address
        self.books = {}
        self.number_employees = 0

    def show_library(self):
        print("Name of library:", self.library_name)
        print("Address:", self.address)
        print("Total Books:", len(self.books))
        print("Total Employee Working:", self.number_employees)

    def add_book(self, book):
        if book.book_id in self.books:
            return False, "Book Already Exists, Please Enter Valid Book Id"
        else:
            self.books[book.book_id] = book
            self.save_books()
            return True, "Book Added Successfully"

    def search_book(self, book_id):
        if book_id not in self.books:
            return None
        else:
            return self.books[book_id]

    def remove_book(self, book_id):
        if book_id not in self.books:
            return False, "Book Id Not Exists Please Enter Valid Id"
        else:
            book = self.books[book_id]
            self.save_deleted_book(book)
            del self.books[book_id]
            self.save_books()
            return True, "Book Removed Successfully"

    def show_all_books(self):
        return list(self.books.values())

    def library_stats(self):
        if len(self.books) == 0:
            return None
        total_books = len(self.books)
        available_books = sum(1 for b in self.books.values() if b.available)
        borrowed_books = total_books - available_books
        return total_books, available_books, borrowed_books

    def search_by_title(self, book_title):
        matched_book = []
        if book_title.strip() == "":
            return []
        for book in self.books.values():
            if book_title.lower() in book.title.lower():
                matched_book.append(book)
        return matched_book

    def search_by_author(self, author):
        matched_author = []
        if author.strip() == "":
            return []
        for book in self.books.values():
            if author.lower() in book.author.lower():
                matched_author.append(book)
        return matched_author

    def check_availability(self, book_id):
        book = self.search_book(book_id)
        if book is not None:
            return book.available
        return None

    def load_book(self):
        try:
            with open("library_data.txt", "r") as file:
                for line in file:
                    data = line.strip().split(",")
                    if len(data) == 4:
                        book_id, title, author, available = data
                        book = Book(int(book_id), title, author, available=available == "True")
                        self.books[int(book_id)] = book
                    else:
                        print("Invalid data format in line:", line)
                        continue
        except FileNotFoundError:
            print("No Book Data Found")

    def borrow_book(self, book_id):
        if book_id not in self.books:
            return False, "Book Not Exist"
        book = self.search_book(book_id)
        if book.available:
            book.available = False
            self.save_books()
            return True, "Book Borrowed Successfully"
        else:
            return False, "Book already borrowed."

    def return_book(self, book_id):
        if book_id not in self.books:
            return False, "Book Not Exist"
        book = self.search_book(book_id)
        if not book.available:
            book.available = True
            self.save_books()
            return True, "Book Returned Successfully"
        else:
            return False, "Book already Returned."

    def save_books(self):
        with open("library_data.txt", "w") as file:
            for b in self.books.values():
                file.write(f"{b.book_id},{b.title},{b.author},{b.available}\n")

    def update_title(self, book_id, new_title):
        if book_id not in self.books:
            return False, "Book Not Exist"
        book = self.search_book(book_id)
        book.update_title(new_title)
        self.save_books()
        return True, "Title Updated Successfully"

    def generate_book_id(self):
        if len(self.books) == 0:
            return 101
        return max(self.books.keys()) + 1

    def save_deleted_book(self, book):
        with open("deleted_books.txt", "a") as file:
            file.write(f"{book.book_id},{book.title},{book.author},{book.available}\n")

    def load_deleted_books(self):
        deleted_books = []
        try:
            with open("deleted_books.txt", "r") as file:
                for line in file:
                    data = line.strip().split(",")
                    if len(data) == 4:
                        book_id, title, author, available = data
                        book = Book(int(book_id), title, author, available=available == "True")
                        deleted_books.append(book)
        except FileNotFoundError:
            print("No Deleted Book Found")
        return deleted_books

    def restore_deleted_book(self, book_id):
        deleted_books = self.load_deleted_books()
        if not deleted_books:
            return False, "No Book Found In Deleted Books"

        for book in deleted_books:
            if book.book_id == book_id:
                if book.book_id in self.books:
                    return False, "Book Already In Library"
                self.books[book.book_id] = book
                self.save_books()
                deleted_books.remove(book)
                with open("deleted_books.txt", "w") as file:
                    for b in deleted_books:
                        file.write(f"{b.book_id},{b.title},{b.author},{b.available}\n")
                return True, "Book Restored Successfully"

        return False, "Book Id Not Found"

    def restore_all_deleted_books(self):
        deleted_books = self.load_deleted_books()
        if not deleted_books:
            return False, "No Deleted Book Found"
        for book in deleted_books:
            if book.book_id not in self.books:
                self.books[book.book_id] = book
        self.save_books()
        with open("deleted_books.txt", "w") as file:
            pass
        return True, "All Deleted Books Restored"


# ----------------------------------------------------------------------
# GUI LAYER
# ----------------------------------------------------------------------
class LibraryGUI:
    def __init__(self, root, library):
        self.root = root
        self.library = library
        self.root.title(f"{library.library_name} - Library Management System")
        self.root.geometry("950x600")
        self.root.minsize(800, 500)

        self._build_layout()
        self.refresh_table()
        self.update_stats()

    # ---------------- layout ----------------
    def _build_layout(self):
        header = tk.Frame(self.root, bg="#2c3e50", pady=12)
        header.pack(fill="x")
        tk.Label(
            header, text=f"📚 {self.library.library_name}", fg="white",
            bg="#2c3e50", font=("Segoe UI", 16, "bold")
        ).pack(side="left", padx=15)
        tk.Label(
            header, text=self.library.address, fg="#bdc3c7",
            bg="#2c3e50", font=("Segoe UI", 10)
        ).pack(side="left")

        # ---- toolbar ----
        toolbar = tk.Frame(self.root, pady=8)
        toolbar.pack(fill="x", padx=10)

        buttons = [
            ("Add Book", self.add_book_dialog),
            ("Remove Book", self.remove_book_dialog),
            ("Borrow", self.borrow_book_dialog),
            ("Return", self.return_book_dialog),
            ("Edit Title", self.update_title_dialog),
            ("Restore Deleted", self.restore_book_dialog),
            ("Restore All", self.restore_all_books),
            ("Refresh", self.refresh_table),
        ]
        for text, cmd in buttons:
            tk.Button(toolbar, text=text, command=cmd, width=14).pack(side="left", padx=3)

        # ---- search bar ----
        search_frame = tk.Frame(self.root, pady=5)
        search_frame.pack(fill="x", padx=10)

        tk.Label(search_frame, text="Search:").pack(side="left")
        self.search_var = tk.StringVar()
        search_entry = tk.Entry(search_frame, textvariable=self.search_var, width=30)
        search_entry.pack(side="left", padx=5)
        search_entry.bind("<Return>", lambda e: self.search_by_title())

        self.search_mode = tk.StringVar(value="title")
        ttk.Combobox(
            search_frame, textvariable=self.search_mode,
            values=["title", "author"], width=8, state="readonly"
        ).pack(side="left", padx=5)

        tk.Button(search_frame, text="Search", command=self.do_search).pack(side="left", padx=5)
        tk.Button(search_frame, text="Clear", command=self.refresh_table).pack(side="left")

        # ---- table ----
        table_frame = tk.Frame(self.root)
        table_frame.pack(fill="both", expand=True, padx=10, pady=5)

        columns = ("id", "title", "author", "available")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings", selectmode="browse")
        for col, label, width in [
            ("id", "Book ID", 80),
            ("title", "Title", 350),
            ("author", "Author", 250),
            ("available", "Available", 100),
        ]:
            self.tree.heading(col, text=label)
            self.tree.column(col, width=width, anchor="w")

        vsb = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=vsb.set)
        self.tree.pack(side="left", fill="both", expand=True)
        vsb.pack(side="right", fill="y")

        # ---- footer / stats ----
        self.stats_label = tk.Label(self.root, text="", font=("Segoe UI", 10), anchor="w")
        self.stats_label.pack(fill="x", padx=15, pady=6)

    # ---------------- helpers ----------------
    def refresh_table(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for book in self.library.show_all_books():
            self.tree.insert(
                "", "end",
                values=(book.book_id, book.title, book.author, "Yes" if book.available else "No"),
            )
        self.update_stats()

    def update_stats(self):
        stats = self.library.library_stats()
        if stats is None:
            self.stats_label.config(text="No books available in the library.")
        else:
            total, available, borrowed = stats
            self.stats_label.config(
                text=f"Total Books: {total}   |   Available: {available}   |   Borrowed: {borrowed}"
            )

    def get_selected_id(self):
        selection = self.tree.selection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select a book from the table first.")
            return None
        values = self.tree.item(selection[0], "values")
        return int(values[0])

    def populate_table(self, books):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for book in books:
            self.tree.insert(
                "", "end",
                values=(book.book_id, book.title, book.author, "Yes" if book.available else "No"),
            )

    # ---------------- actions ----------------
    def add_book_dialog(self):
        title = simpledialog.askstring("Add Book", "Enter Book Title:", parent=self.root)
        if not title:
            return
        author = simpledialog.askstring("Add Book", "Enter Author Name:", parent=self.root)
        if not author:
            return
        book_id = self.library.generate_book_id()
        book = Book(book_id, title, author)
        success, msg = self.library.add_book(book)
        if success:
            messagebox.showinfo("Success", f"{msg}\nGenerated Book Id: {book_id}")
        else:
            messagebox.showerror("Error", msg)
        self.refresh_table()

    def remove_book_dialog(self):
        book_id = self.get_selected_id()
        if book_id is None:
            return
        if not messagebox.askyesno("Confirm", f"Remove book ID {book_id}?"):
            return
        success, msg = self.library.remove_book(book_id)
        messagebox.showinfo("Result", msg) if success else messagebox.showerror("Error", msg)
        self.refresh_table()

    def borrow_book_dialog(self):
        book_id = self.get_selected_id()
        if book_id is None:
            return
        success, msg = self.library.borrow_book(book_id)
        messagebox.showinfo("Result", msg) if success else messagebox.showerror("Error", msg)
        self.refresh_table()

    def return_book_dialog(self):
        book_id = self.get_selected_id()
        if book_id is None:
            return
        success, msg = self.library.return_book(book_id)
        messagebox.showinfo("Result", msg) if success else messagebox.showerror("Error", msg)
        self.refresh_table()

    def update_title_dialog(self):
        book_id = self.get_selected_id()
        if book_id is None:
            return
        new_title = simpledialog.askstring("Edit Title", "Enter New Title:", parent=self.root)
        if not new_title:
            return
        success, msg = self.library.update_title(book_id, new_title)
        messagebox.showinfo("Result", msg) if success else messagebox.showerror("Error", msg)
        self.refresh_table()

    def restore_book_dialog(self):
        book_id = simpledialog.askinteger("Restore Book", "Enter Book Id to restore:", parent=self.root)
        if book_id is None:
            return
        success, msg = self.library.restore_deleted_book(book_id)
        messagebox.showinfo("Result", msg) if success else messagebox.showerror("Error", msg)
        self.refresh_table()

    def restore_all_books(self):
        if not messagebox.askyesno("Confirm", "Restore all deleted books?"):
            return
        success, msg = self.library.restore_all_deleted_books()
        messagebox.showinfo("Result", msg) if success else messagebox.showerror("Error", msg)
        self.refresh_table()

    def do_search(self):
        if self.search_mode.get() == "title":
            self.search_by_title()
        else:
            self.search_by_author()

    def search_by_title(self):
        query = self.search_var.get()
        results = self.library.search_by_title(query)
        if not results:
            messagebox.showinfo("Search", "No books found.")
            self.refresh_table()
        else:
            self.populate_table(results)

    def search_by_author(self):
        query = self.search_var.get()
        results = self.library.search_by_author(query)
        if not results:
            messagebox.showinfo("Search", "No books found.")
            self.refresh_table()
        else:
            self.populate_table(results)


def main():
    library = Library("Mumbai Library", "Mumbai")
    library.load_book()
    library.load_deleted_books()

    root = tk.Tk()
    app = LibraryGUI(root, library)
    root.mainloop()


if __name__ == "__main__":
    main()
