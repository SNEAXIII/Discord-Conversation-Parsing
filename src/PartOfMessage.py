from abc import ABC, abstractmethod


class PartOfMessage(ABC):
    def __init__(self,rawString):
        self.rawString = rawString
        xBase = 68

    @abstractmethod
    def show(self):
        pass
