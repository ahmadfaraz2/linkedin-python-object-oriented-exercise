# Python Object Oriented Programming by Joe Marini course example
# Creating immutable data classes

from dataclasses import dataclass


@dataclass(frozen=True)  # TODO: "The "frozen" parameter makes the class immutable
class ImmutableClass:
    value1: str = "Value 1"
    value2: int = 0

    def some_func(self, new_val):
        self.value1 = new_val


obj = ImmutableClass("It's a new value", 50)
print(obj.value1, obj.value2)

# TODO: attempting to change the value of an immutable class throws an exception
# obj.value2 = 10
# print(obj)

# TODO: even functions within the class can't change anything
# obj.some_func("New value")
