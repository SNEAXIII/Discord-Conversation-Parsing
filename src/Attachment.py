from src.PartOfMessage import PartOfMessage


class Attachment(PartOfMessage):
    def __init__(self,strAttachmentUrl):
        super().__init__(strAttachmentUrl)

    def show(self):
        print("Implémentation de la méthode abstraite")
