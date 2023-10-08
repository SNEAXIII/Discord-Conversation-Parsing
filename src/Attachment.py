from PartOfMessage import PartOfMessage


class Attachment(PartOfMessage):
    def __init__(self,rawString):
        super().__init__(rawString)

    def show(self):
        print("Implémentation de la méthode abstraite")
