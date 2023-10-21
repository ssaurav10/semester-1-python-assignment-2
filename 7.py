"""

#question
Write a Python program to create a class named Book with attributes title, author and
price. Implement methods to display the book's information and apply a discount on the
price. Also, implement a subclass named EBook with an additional attribute format.
Override the display method for the EBook subclass.

"""

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nPrice: ${self.price:.2f}"

    def apply_discount(self, discount_percent):
        if 0 <= discount_percent <= 100:
            self.price -= (self.price * discount_percent / 100)
            return f"{discount_percent}% discount applied. New price: ${self.price:.2f}"
        else:
            return "Invalid discount percentage."

class EBook(Book):
    def __init__(self, title, author, price, ebook_format):
        super().__init__(title, author, price)
        self.format = ebook_format

    def display(self):
        book_info = super().display()
        return f"{book_info}\nFormat: {self.format}"

book1 = Book("The Catcher in the Rye", "J.D. Salinger", 15.99)
ebook1 = EBook("Python for Beginners", "John Smith", 9.99, "PDF")

print("Book Information:")
print(book1.display())

print("\nEBook Information:")
print(ebook1.display())

book1.apply_discount(10)
print("\nDiscount Applied to Book:")
print(book1.display())

ebook1.apply_discount(20)
print("\nDiscount Applied to EBook:")
print(ebook1.display())