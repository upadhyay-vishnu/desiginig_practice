"""
We are implementing a Coffee shop,
let's say we have few type of coffees- Cappuccino, Espresso, Latte, Decaf
User has liberty to add the condiments and modify the coffee according to their need.

We are going to use decorator pattern, where each condiement is explicitely added to the coffee.
c = Cappuccino()
c.decorate(m)

"""

from abc import ABCMeta, abstractmethod

class BeverageAbstract(metaclass=ABCMeta):
    @abstractmethod
    def get_description(self):
        NotImplementedError

    @abstractmethod
    def get_cost(self):
        NotImplementedError


class CondimentDecorator(BeverageAbstract):
    pass


class Cappuccino(BeverageAbstract):

    def __init__(self):
        self.cost = 55
        self.description = "Cappuccino"

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost

    def add_condiment(self, condiement: CondimentDecorator):
        self.cost += condiement.get_cost()
        self.description = self.description + ' ' + condiement.get_description()


class Milk(CondimentDecorator):
    # Condiment doesn't have it's own value or sell so if the initialization
    # happening without a beverage then it's wrong
    def get_description(self):
        return "Milk"

    def get_cost(self):
        return 10


class Chocochip(CondimentDecorator):
    def get_description(self):
        return "Chocochip"

    def get_cost(self):
        return 10


if __name__ == '__main__':
    bev = Cappuccino()
    bev.add_condiment(Milk())
    bev.add_condiment(Chocochip())
    print(bev.get_cost())
    print(bev.get_description())
