import json
import os
import datetime


class Base:
    def __init__(self, name):
        self.name       = name
        self.created_at = str(datetime.datetime.now())
        self.updated_at = self.created_at

    def save(self):
        self.updated_at = str(datetime.datetime.now())
        with open(f"{self.name}.json", "w") as f:
            json.dump(self.__dict__, f, indent=2)

    def load(self):
        with open(f"{self.name}.json") as f:
            data = json.load(f)
        self.__dict__.update(data)


class Book(Base):
    def __init__(self, name, author, year, genre):
        Base.__init__(self, name)
        self.author      = author
        self.year        = year
        self.genre       = genre
        self.is_borrowed = False

        if os.path.exists(f"{self.name}.json"):
            self.load()
        else:
            self.save()

        self.is_borrowed = False
        self.save()


class User(Base):
    def __init__(self, name, user_id):
        Base.__init__(self, name)
        self.user_id = user_id

        if os.path.exists(f"{self.name}.json"):
            self.load()
        else:
            self.save()

    def borrow_book(self, book):
        if not book.is_borrowed:
            book.is_borrowed = True
            book.save()
            print(f"{self.name} has borrowed '{book.name}'")
        else:
            print(f"Sorry {self.name}, '{book.name}' is already borrowed")


# --- Run ---

bookOne   = Book("The Lost River", author="Jack", year=2005, genre="Fiction")
bookTwo   = Book("Dark Skies",     author="Eric", year=2010, genre="Novel")
bookThree = Book("Quiet Roads",    author="Anna", year=1998, genre="Classic")

userOne = User("John",  user_id="001")
userTwo = User("Sarah", user_id="002")

userOne.borrow_book(bookOne)
userTwo.borrow_book(bookOne)
userTwo.borrow_book(bookTwo)