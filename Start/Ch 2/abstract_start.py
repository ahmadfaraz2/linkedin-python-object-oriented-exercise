# Python Object Oriented Programming by Joe Marini course example
# Using Abstract Base Classes to enforce class constraints

from abc import ABC, abstractmethod


class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod  # This will enforce other subclasses to use it
    def calcArea(self):
        pass


class Circle(GraphicShape):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return 3.14 * (self.radius**2)


class Square(GraphicShape):
    def __init__(self, side):
        self.side = side

    def calcArea(self):
        return self.side * self.side


# g = GraphicShape() # So the class that are child class of "ABC" can't be instantiate

c = Circle(10)
print(c.calcArea())
s = Square(12)
print(s.calcArea())


"""
    So we can use Abstraction where we want to make a Base class
    but we don't want to make instances of this class but we can
    enforce the constraints that there are certain methods in
    the Base class that have to be implemented in subclasses.
"""
