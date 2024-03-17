# Python Object Oriented Programming by Joe Marini course example
# Using instance methods and attributes


class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title, author, pages, price):
        self.title = title
        # TODO: add properties
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = "This is a secret attribute."

    # TODO: create instance methods
    def get_price(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price

    def setdiscount(self, amount):
        self._discount = amount


# TODO: create some book instances
b1 = Book("The One Thing", "Gary Keller and Jay Papson", 240, 50.0)
b2 = Book("Sometimes You Win, Sometimes You Learn", "John C. Maxwell", 116, 30.0)

# TODO: print the price of book1
# print(b1.title, " by " + b1.author)
# print(b1.get_price())

# TODO: try setting the discount
print(b2.get_price())
b2.setdiscount(0.25)
print(b2.get_price())


# TODO: properties with double underscores are hidden by the interpreter
print(b1._Book__secret)

# -------------------------------------Learning--------------------------------------

"""( _ ) underscore in front of any attribute and method:

    It ( _ ) is used to give other developers a hint that this attribute is considered internal to the class and is not for public consumption. It tells don't use this (attribute / method) outside this class."""
