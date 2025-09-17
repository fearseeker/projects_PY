from abc import ABC, abstractmethod

class Subject(ABC):
    @abstractmethod
    def request(self, amount) -> None:
        pass

class RealSubject(Subject):
    def __init__(self, money = 100):
        self.money = money

    def request(self, amount) -> None:
        self.money -= amount
        print(f"Деньги переведены: {amount}. Остаток: {self.money}")

class Proxy(RealSubject):
    def __init__(self, real_subject: RealSubject):
        self._real_subject = real_subject

    def request(self, amount) -> None:
        if self._real_subject.money >= amount:
            self._real_subject.request(amount)
        else:
            print(f"Недостаточно денег! Баланс: {self._real_subject.money}, нужно: {amount}")

def client_code(subject: Subject, amount) -> None:
    subject.request(amount)

if __name__ == '__main__':

    real_sub = RealSubject()
    proxy = Proxy(real_sub)

    client_code(proxy, 50)
    client_code(proxy, 40)
    client_code(proxy, 50)
    print(f"Денег у реального объекта: {real_sub.money}")


