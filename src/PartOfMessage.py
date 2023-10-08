from abc import ABC, abstractmethod


class PartOfMessage(ABC):
    def __init__(self,rawstring):
        self.rawstring = rawstring

    @abstractmethod
    def show(self):
        pass
