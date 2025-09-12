from abc import ABC, abstractmethod

class Creator(ABC):

    @abstractmethod
    def get_Inform(self):
        pass

class Game1(Creator):
    def __init__(self):
        self.name = "dota2"
        self.reit = 2000
        self.hour = 5000
    def get_Inform(self):
        return {"Вы запустили: ": self.name, "У вас столько: ": str(self.reit) + " ММР",
            "Вы наиграли в игру: ": str(self.hour) + " часов"}

class Game2(Creator):
    def __init__(self):
        self.name = "CsGo"
        self.reit = 5500
        self.hour = 15000
    def get_Inform(self):
        return {"Вы запустили: ": self.name, "У вас столько: ": str(self.reit) + " ММР",
            "Вы наиграли в игру: ": str(self.hour) + " часов"}


class ChosseGame():
    def get_game(self, game_number):
        if game_number == 1:
            return Game1()
        if game_number == 2:
            return Game2()

if __name__ == '__main__':
    chooser = ChosseGame()
    game1 = chooser.get_game(1)
    game2 = chooser.get_game(2)
    print(game1.get_Inform())
    print(game2.get_Inform())



