from abc import ABC, abstractmethod

class Notifier(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailNotifier(Notifier):
    def send(self, message):
        print(f"Отправка EMAIL: {message}")

class NotifierDecorator(Notifier):
    def __init__(self, wrapped: Notifier):
        self._wrapped = wrapped

    def send(self, message):
        self._wrapped.send(message)

class SMSNotifier(NotifierDecorator):
    def send(self, message):
        super().send(message)
        print(f"Отправка SMS: {message}")

class ViberNotifier(NotifierDecorator):
    def send(self, message):
        super().send(message)
        print(f"Отправка в Slack: {message}")


if __name__ == "__main__":

    base_notifier = EmailNotifier()
    sms_notifier = SMSNotifier(base_notifier)
    full_notifier = ViberNotifier(sms_notifier)

    print("Отправка через Email ")
    base_notifier.send("Hello World!")
    print("\nОтправка через Email + SMS ")
    sms_notifier.send("Hello World!")
    print("\nОтправка через Email + SMS + Viber")
    full_notifier.send("Hello World!")