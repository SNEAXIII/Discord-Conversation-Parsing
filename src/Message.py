from datetime import datetime

from src.PieceJointe import PieceJointe
from src.Text import Text


class Message:
    def __init__(self, listRawContent, auteur):
        _id, rawStrTimestamp, rawStrMessage, rawStrAttachments = listRawContent
        self.id = int(_id)
        self.dateTime = datetime.fromisoformat(rawStrTimestamp)
        self.text = Text(rawStrMessage)
        self.attachments = self.getAttachments(rawStrAttachments)
        self.auteur = auteur
        self.y = None

    def __str__(self):
        result = " ".join([self.auteur.nom, self.dateToString(), "-->"])
        if self.isHaveText():
            return " ".join([result, self.text.rawString])
        return " ".join([result, "C'est vide"])

    @staticmethod
    def getAttachments(rawString):
        result = []
        if rawString:
            listAttachments = rawString.split(" ")
            for attachmentUrl in listAttachments:
                result.append(PieceJointe(attachmentUrl))
        return result

    def isHaveText(self):
        return bool(not self.text.isEmpty())

    def isHaveAttachment(self):
        return bool(self.attachments)

    def dateToString(self):
        return self.dateTime.strftime("%d/%m/%Y %H:%M")

    def setY(self, y):
        self.y = y

    # TODO
    def show(self):
        pass
