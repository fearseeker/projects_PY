class LightWeight:
    def __init__(self, char):
        self.char = char

    def display(self, font_size):
        print(f"Символ: {self.char} с размером шрифта {font_size}")


class LightWeightFactory:
    _flyweights = {}

    def get_char(cls, char) -> LightWeight:
        if char not in cls._flyweights:
            cls._flyweights[char] = LightWeight(char)
        return cls._flyweights[char]


if __name__ == "__main__":

    factory = LightWeightFactory()

    c1 = factory.get_char("A")
    c2 = factory.get_char("A")
    c3 = factory.get_char("B")

    print(f"c1 is c2 {c1 is c2}")
    print(f"c1 is c3 {c1 is c3}")

    c1.display(12)
    c2.display(18)
    c3.display(14)