from abc import ABC, abstractmethod

class Burger:
    def __init__(self):
        self.bun = None
        self.meat = None
        self.salad = False
        self.tomato = False
        self.cheese = False
        self.sauce = False

    def __str__(self):
        ingredients = []
        if self.bun:
            ingredients.append(f"Булка: {self.bun}")
        if self.meat:
            ingredients.append(f"М`ясо: {self.meat}")
        if self.salad:
            ingredients.append("Салат")
        if self.tomato:
            ingredients.append("Помідор")
        if self.cheese:
            ingredients.append("Сир")
        if self.sauce:
            ingredients.append("Соус")
        return "Бургер с: " + ", ".join(ingredients)

class BurgerBuilder(ABC):
    def __init__(self):
        self.burger = Burger()

    @abstractmethod
    def set_bun(self, bun): pass

    @abstractmethod
    def set_meat(self, meat): pass

    @abstractmethod
    def add_salad(self, has): pass

    @abstractmethod
    def add_tomato(self, has): pass

    @abstractmethod
    def add_cheese(self, has): pass

    @abstractmethod
    def add_sauce(self, has): pass

    def get_result(self):
        return self.burger

class CustomBurgerBuilder(BurgerBuilder):
    def set_bun(self, bun):
        self.burger.bun = bun

    def set_meat(self, meat):
        self.burger.meat = meat

    def add_salad(self, has):
        self.burger.salad = has

    def add_tomato(self, has):
        self.burger.tomato = has

    def add_cheese(self, has):
        self.burger.cheese = has

    def add_sauce(self, has):
        self.burger.sauce = has
if __name__ == "__main__":
    builder1 = CustomBurgerBuilder()

    builder1.set_bun("Ржана чорна булка")
    builder1.set_meat("Соковита яловичина")
    builder1.add_salad(True)
    builder1.add_tomato(True)
    builder1.add_cheese(False)
    builder1.add_sauce(False)

    burger1 = builder1.get_result()
    print(burger1)

    builder2 = CustomBurgerBuilder()

    builder2.set_bun("біла булка")
    builder2.set_meat("Соковита курка")
    builder2.add_salad(False)
    builder2.add_tomato(True)
    builder2.add_cheese(True)
    builder2.add_sauce(True)

    burger2 = builder2.get_result()
    print(burger2)