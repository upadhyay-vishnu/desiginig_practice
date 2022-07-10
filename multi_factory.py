"""
Pizza store is open to multiple place and give them flexibility to create pizza of there own choice,
But the order will go through the interface which will remain constant.

so we have DelhiPizzaStore, BanglorePizzaStore
Pizza Store fixed the interface
"""

class PizzaStore:
    def order_pizza(self, pizza_type):
        self.pizza.prepare()
        self.pizza.bake()
        self.pizza.box()


class Pizza:
    def prepare(self):
        print("preparing")

    def bake(self):
        print("baking")

    def box(self):
        print("wrapping")


class DelhiPizza(Pizza):
    pass


class DelhiCheesePizza(DelhiPizza):
    pass


class BanglorePizza(Pizza):
    pass


class BangloreCheesePizza(BanglorePizza):
    pass


class DelhiPizzaFactory:
    @classmethod
    def create_pizza(self, pizza_type):
        if pizza_type == 'Cheese':
            print("Here comes your Cheese Pizza")
            return DelhiCheesePizza()


class BanglorePizzaFactory:
    @classmethod
    def create_pizza(self, pizza_type):
        if pizza_type == 'Cheese':
            print("Here comes your Cheese Pizza")
            return BangloreCheesePizza()


class DelhiPizzaStore(PizzaStore):
    # def __init__(self):
    #     print("Delhi Pizza Store Welcomes you:- " )
    #     self.factory = DelhiPizzaFactory()

    def order_pizza(self, pizza_type):
        self.pizza = DelhiPizzaFactory.create_pizza(pizza_type)
        super().order_pizza(pizza_type)


class BanglorePizzaStore(PizzaStore):
    def __init__(self):
        self.factory = BanglorePizzaStore()

    def order_pizza(self, pizza_type):
        self.pizza = self.factory.create_pizza()
        super().order_pizza(pizza_type)


if __name__ == '__main__':
    d = DelhiPizzaStore()
    d.order_pizza("Cheese")
