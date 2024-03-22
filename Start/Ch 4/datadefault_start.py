# Python Object Oriented Programming by Joe Marini course example
# implementing default values in data classes

from dataclasses import dataclass, field
import random


def func_price():
    randint = random.randrange(20, 40)
    return randint


@dataclass
class Book:
    # you can define default values when attributes are declared
    title: str = "No Title"
    author: str = "No Author"
    pages: int = 0
    # price: float = field(default=10.0)
    price: float = field(default_factory=func_price)


b1 = Book()
print(b1)

b2 = Book("The One Thing", "Gary Keller and J.Papason", 240)
b3 = Book("Sometimes You Win Sometimes You Lose", "John C.Maxwell", 250)


print(b2)
print(b3)
