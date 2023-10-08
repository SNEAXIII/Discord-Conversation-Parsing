from abc import ABC, abstractmethod


class PartOfMessage(ABC):
    def __init__(self,rawString):
        self.rawString = rawString

    @abstractmethod
    def show(self):
        pass
