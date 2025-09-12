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

class Director:
    def __init__(self, builder: BurgerBuilder):
        self.builder = builder

    def create_beef_burger(self):
        self.builder.set_bun("Ржана чорна булка")
        self.builder.set_meat("Соковита яловичина")
        self.builder.add_salad(True)
        self.builder.add_tomato(True)
        self.builder.add_cheese(False)
        self.builder.add_sauce(False)
        return self.builder.get_result()

    def create_chicken_burger(self):
        self.builder.set_bun("Біла булка")
        self.builder.set_meat("Соковита курка")
        self.builder.add_salad(False)
        self.builder.add_tomato(True)
        self.builder.add_cheese(True)
        self.builder.add_sauce(True)
        return self.builder.get_result()

# === Использование ===
if __name__ == "__main__":
    builder = CustomBurgerBuilder()
    director = Director(builder)

    # Автоматическая сборка по "рецепту"
    burger1 = director.create_beef_burger()
    print(burger1)

    burger2 = director.create_chicken_burger()
    print(burger2)


