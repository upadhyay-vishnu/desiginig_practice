"""
Here we are implementing Duck Behaviour,
Duck has
    Swim
    Quack
    disply

Duck Type:
    Mallard Duck
    Rubber Duck (Can't quack)
    RocketDuck - which actually can fly with some support

So behaviour distributed amond some categories
"""

"""
Implementing Behaviours
"""


from abc import ABCMeta, abstractmethod


class FlyBehaviour(metaclass=ABCMeta):
    @abstractmethod
    def fly(self):
        NotImplementedError


class SwimBehaviour(metaclass=ABCMeta):
    @abstractmethod
    def swim(self):
        NotImplementedError


class QuackBehaviour(metaclass=ABCMeta):
    @abstractmethod
    def quack(self):
        NotImplementedError


class Fly(FlyBehaviour):
    def fly(self):
        print("I am flying")


class NoFly(FlyBehaviour):
    def fly(self):
        pass


class Swim(SwimBehaviour):
    def swim(self):
        print("I am swimming")


class NoSwim(SwimBehaviour):
    def swim(self):
        pass


class Quack(QuackBehaviour):
    def quack(self):
        print("Quack")


class Squack(QuackBehaviour):
    def quack(self):
        print("squack")


class Duck:

    def disply(self):
        pass

    def swim(self):
        pass

    def quack(self):
        pass


class Duck2:

    def __init__(self):
        self.quack_behav: QuackBehaviour = None

    def disply(self):
        pass

    def quack(self):
        """
        Delegation of funcionality
        """
        self.quack_behav.quack()

    def set_quack_behavior(self, qb: QuackBehaviour):
        """
        Dynamic behaviour set
        """
        self.quack_behav = qb


class MallardDuck(Duck):
    def disply(self):
        print("I am a mallar duck")

    def swim(self):
        swim_behav = Swim()
        swim_behav.swim()

    def quack(self):
        quack_behav = Quack()
        quack_behav.quack()


class RubberDuck(Duck2):
    def __init__(self):
        self.quack_behav = Squack()

    def disply(self):
        print("I am a rubber duck")
