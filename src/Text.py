from src.PartOfMessage import PartOfMessage


class Text(PartOfMessage):
    def __init__(self, rawString):
        super().__init__(rawString)

    def isEmpty(self):
        return bool(self.rawString.strip())


    def show(self):
        print("Implémentation de la méthode abstraite")
