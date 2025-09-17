class DVDPlayer:
    def on(self):
        print("DVD включен")

    def play(self, movie):
        print(f"Воспроизведение фильма: {movie}")

    def off(self):
        print("DVD выключен")


class Projector:
    def on(self):
        print("Проектор включен")

    def wide_screen_mode(self):
        print("Установлен широкоформатный режим")

    def off(self):
        print("Проектор выключен")


class Amplifier:
    def on(self):
        print("Усилитель включен")

    def set_volume(self, level):
        print(f"Громкость установлена на {level}")

    def off(self):
        print("Усилитель выключен")


class HomeTheaterFasade:
    def __init__(self, dvd: DVDPlayer, projector: Projector, amp: Amplifier):
        self.dvd = dvd
        self.projector = projector
        self.amp = amp

    def watch_movie(self, movie):
        print("Готовимся смотреть фильм...")
        self.projector.on()
        self.projector.wide_screen_mode()
        self.amp.on()
        self.amp.set_volume(5)
        self.dvd.on()
        self.dvd.play(movie)

    def end_movie(self):
        print("Выключаем кинотеатр...")
        self.dvd.off()
        self.amp.off()
        self.projector.off()

if __name__ == "__main__":
    dvd = DVDPlayer()
    projector = Projector()
    amp = Amplifier()

    home_theater = HomeTheaterFasade(dvd, projector, amp)
    home_theater.watch_movie("Матрица")
    print()
    home_theater.end_movie()