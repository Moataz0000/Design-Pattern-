from abc import ABC, abstractmethod
from typing import List


class Observer(ABC):
    """Abstract Observer interface"""
    @abstractmethod
    def update(self, message: str) -> None:
        pass


class EmailNotifier(Observer):
    """Subject: Profile"""
    def __init__(self, recipient_email: str):
        self.recipient_email = recipient_email

    def update(self, message: str) -> None:
        print(f"Sending Email to {self.recipient_email}: {message}")


class Profile:
    def __init__(self):
        self._observers: List[Observer] = []
        self._name: str = ""
    
    def attach(self, observer: Observer) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self, message: str) -> None:
        for observer in self._observers:
            observer.update(message)

    def create_profile(self, name: str) -> None:
        self._name = name
        print(f"Profile created for {self._name}")
        self.notify(f"New profile created for {self._name}")


def main():
    profile = Profile()

    email_notification1 = EmailNotifier(recipient_email="mezo@gmail.com")
    email_notification2 = EmailNotifier(recipient_email="moataz@gmail.com")

    profile.attach(email_notification1)
    profile.attach(email_notification2)

    profile.create_profile("Mezo Da Ana")

    profile.detach(email_notification2)
    print("\nCreating another profile...")
    profile.create_profile("Jane Smith")


if __name__ == "__main__":
    main()