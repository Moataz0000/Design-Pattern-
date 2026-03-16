from typing import List
"""
The Observer Design Pattern is a behavioral design pattern
used when one object needs to notify many other objects automatically whenever its state changes.

The Design Structure
    - Subject (Publisher)
        - Keeps a list of observers
        - Notifies them when something changes
    - Observer (Subscriber)
        - Receives updates
"""

class Observer:
    def update(self, subject: Subject) -> None:
        pass



class Subject:
    _observers = List[Observer]

    def __init__(self) -> None:
        self._observers = []

    
    def attach(self, observer: Observer) -> None:
        if observer not in self._observers:
            self._observers.append(observer)
    
    def detach(self, observer: Observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)