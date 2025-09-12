from abc import ABC, abstractmethod
import copy
class RealOne(ABC):

    @abstractmethod
    def clone(self):
        pass

    @abstractmethod
    def deepcopy(self):
        pass

class Clone(RealOne):
    def __init__(self, name, number, items):
        self.name = name
        self.number = number
        self.items = items if items else []

    def clone(self):
        return Clone(self.name, self.number, self.items)

    def deepcopy(self):
        return Clone(self.name, self.number, self.items.copy())

    def add_item(self, item):
        self.items.append(item)

    def __str__(self):
        return f"Character(name='{self.name}', level={self.number}, items={self.items})"




c1 = Clone("aboba", 12, ["Пушка"])
#всё поверх
c2 = c1.clone()
c2.add_item("Пистоль")
#глубоко(ауф)
c3 = c1.deepcopy()
c3.add_item("Перо")
print("Оригинал:", c1)
print("Shallow:", c2)
print("Deep:", c3)
