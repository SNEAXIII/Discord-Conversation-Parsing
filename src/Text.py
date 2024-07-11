from src.ElementMessage import ElementMessage


class Text(ElementMessage):
    def __init__(self, rawString):
        super().__init__(rawString)
        self.boiteTexte = None

    def isEmpty(self) -> bool:
        return not bool(self.rawString.strip())

    def __str__(self):
        return self.rawString

    def setBoiteText(self, boiteTexte: str) -> None:
        self.boiteTexte = boiteTexte

    def show(self) -> str:
        return self.__str__()
