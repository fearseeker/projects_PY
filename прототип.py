class RealOne():
    def clone(self):

        raise NotImplementedError("Ало, метод то надо реализовать")

class Clone(RealOne):
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def clone(self):
        return Clone(self.name, self.number)

c1 = Clone("aboba", 12)
c2 = c1.clone()
print(c1.name, c1.number)
print(c2.name, c2.number)

