from abc import ABC, abstractmethod

class Game(ABC):
    @abstractmethod
    def type_game(self):
        pass

class Dota(Game):
    def type_game(self):
        return "Dota2 - Moba игра от Valve"

class CsGo(Game):
    def type_game(self):
        return "CS:GO - шутер игра от Valve"

class League(Game):
    def type_game(self):
        return "League of Legends - Moba игра от Riot"

class Valorant(Game):
    def type_game(self):
        return "Valorant - шутер игра от Riot"

class GameFactory(ABC):
    @abstractmethod
    def create_game(self):
        pass

class MobaFactory(GameFactory):
    def __init__(self, game_type):
        self.game_type = game_type

    def create_game(self):
        if self.game_type == "dota":
            return Dota()
        if self.game_type == "league":
            return League()


class ShooterFactory(GameFactory):
    def __init__(self, game_type):
        self.game_type = game_type

    def create_game(self):
        if self.game_type == "csgo":
            return CsGo()
        if self.game_type == "valorant":
            return Valorant()


class GameClient:
    def __init__(self, factory: GameFactory):
        self.factory = factory

    def play_game(self):
        game = self.factory.create_game()
        print(f"Запускаем игру: {game.type_game()}")

if __name__ == "__main__":
    print("MOBA игры ")
    moba_factory = MobaFactory("dota")
    client1 = GameClient(moba_factory)
    client1.play_game()

    moba_factory2 = MobaFactory("league")
    client2 = GameClient(moba_factory2)
    client2.play_game()

    print("\nShooter игры ")
    shooter_factory = ShooterFactory("csgo")
    client3 = GameClient(shooter_factory)
    client3.play_game()

    shooter_factory2 = ShooterFactory("valorant")
    client4 = GameClient(shooter_factory2)
    client4.play_game()