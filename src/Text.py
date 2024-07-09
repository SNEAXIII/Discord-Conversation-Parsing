from src.ElementMessage import ElementMessage


class Text(ElementMessage):
    def __init__(self, rawString):
        super().__init__(rawString)

    def isEmpty(self):
        return not bool(self.rawString.strip())

    def __str__(self):
        return self.rawString

    def show(self):
        return self.__str__()
