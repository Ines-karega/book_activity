import json
import os
import datetime


class Base:
    def __init__(self, name):
        self.file = f"{name}.json"

        if os.path.exists(self.file):
            with open(self.file) as f:
                data = json.load(f)
            for key, value in data.items():
                setattr(self, key, value)
            print(f"Loaded {self.file}")
        else:
            self.id = name                              # simple, readable ID
            self.created_at = str(datetime.datetime.now())
            self.updated_at = self.created_at

    def save(self):
        self.updated_at = str(datetime.datetime.now())
        with open(self.file, "w") as f:
            json.dump(self.__dict__, f, indent=2)
        print(f"Saved {self.file}")


class Book(Base):
    def __init__(self, name, title, author, genre):
        Base.__init__(self, name)       # same as super().__init__(name)
        if not os.path.exists(self.file):
            self.title = title
            self.author = author
            self.genre = genre
            self.is_borrowed = False


class User(Base):
    def __init__(self, name, username, email):
        Base.__init__(self, name)
        if not os.path.exists(self.file):
            self.username = username
            self.email = email

    def borrow(self, book):
        if book.is_borrowed:
            print(f"'{book.title}' is already borrowed — not available")
        else:
            book.is_borrowed = True
            book.save()
            print(f"'{book.title}' was borrowed by {self.username}")

    def return_book(self, book):
        if not book.is_borrowed:
            print(f"'{book.title}' was not borrowed — nothing to return")
        else:
            book.is_borrowed = False
            book.save()
            print(f"'{book.title}' was returned by {self.username}")


# --- Run ---

book1 = Book("book1", title="Clean Code", author="Robert Martin", genre="Programming")
book1.save()

user1 = User("user1", username="Alice", email="alice@email.com")
user1.save()

user1.borrow(book1)       # borrows it
user1.borrow(book1)       # already borrowed
user1.return_book(book1)  # returns it
user1.return_book(book1)  # already returned