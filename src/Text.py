from src.ElementMessage import ElementMessage


class Text(ElementMessage):
    def __init__(self, rawString):
        super().__init__(rawString)

    def isEmpty(self) -> bool:
        return not bool(self.rawString.strip())

    def __str__(self):
        return self.rawString

    def show(self) -> str:
        return self.__str__()
