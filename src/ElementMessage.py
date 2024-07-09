from abc import ABC, abstractmethod


class ElementMessage(ABC):
    def __init__(self, rawString):
        self.rawString = rawString

    @abstractmethod
    def show(self):
        pass
