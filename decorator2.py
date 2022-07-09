"""
this is going to be slightly different then previous,
Here we predefine the 
"""

from abc import ABCMeta, abstractmethod


class BeverageAbstract(metaclass=ABCMeta):
    @abstractmethod
    def get_description(self):
        NotImplementedError

    @abstractmethod
    def get_cost(self):
        NotImplementedError


class Beverage(BeverageAbstract):
    pass


class CondimentDecorator(Beverage):
    beverage: Beverage


class Cappuccino(Beverage):

    def __init__(self):
        self.cost = 55
        self.description = "Cappuccino"

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost


class Milk(CondimentDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + " Milk"

    def get_cost(self):
        return self.beverage.get_cost() + 10


class Foo:
    pass


class ChocoChip(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + " Chip"

    def get_cost(self):
        return self.beverage.get_cost() + 10


if __name__ == '__main__':
    f = Foo()
    ChocoChip(f)
    cap = Cappuccino()
    cap = ChocoChip(Milk(cap))
    print(type(cap))
    print(cap.get_description())
    print(cap.get_cost())

