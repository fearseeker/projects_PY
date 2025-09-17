from abc import ABC, abstractmethod

class Color(ABC):
    @abstractmethod
    def fill(self):
        pass

class RedColor(Color):
    def fill(self):
        return "красным цветом"

class BlueColor(Color):
    def fill(self):
        return "синим цветом"

class Shape(ABC):
    def __init__(self, color: Color):
        self.color = color
    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print(f"Рисуем круг {self.color.fill()}")

class Square(Shape):
    def draw(self):
        print(f"Рисуем квадрат {self.color.fill()}")

if __name__ == "__main__":
    red = RedColor()
    blue = BlueColor()

    red_circle = Circle(red)
    blue_circle = Circle(blue)
    red_square = Square(red)
    blue_square = Square(blue)

    red_circle.draw()
    blue_circle.draw()
    red_square.draw()
    blue_square.draw()