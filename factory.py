"""
Here we are implementing Pizza store.
Pizza Store has distributed pizza prepration in following set
1: Prepare
2: Bake
3: cut
4: Box

Pizza can be of any type, Cheese, double cheese, Vegeroma, Paneer

So, Customer comes to Pizza store and orders a pizza
"""


class Pizza:
    def prepare(self):
        print("preparing")

    def bake(self):
        print("baking")

    def box(self):
        print("wrapping")


class CheesPizza(Pizza):
    pass


class PaneerPizaa(Pizza):
    pass


class PizzaFactory:
    def get_pizza(self, pizza_type):
        if pizza_type == 'Cheese':
            return CheesPizza()
        elif pizza_type == 'Paneer':
            return PaneerPizaa()


class PizzaStore:
    pizza = None

    def __init__(self):
        self.factory = PizzaFactory()

    def order_pizza(self, pizza_type):
        self.pizza = self.factory.get_pizza(pizza_type)

    def prepare(self):
        self.pizza.prepare()

    def bake(self):
        self.pizza.bake()

    def box(self):
        self.pizza.box()
