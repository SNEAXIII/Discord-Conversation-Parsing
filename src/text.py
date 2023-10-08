from PartOfMessage import PartOfMessage


class Text(PartOfMessage):
    def __init__(self,rawString):
        super().__init__(rawString)

    def show(self):
        print("Implémentation de la méthode abstraite")
