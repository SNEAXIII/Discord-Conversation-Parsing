from datetime import datetime,timedelta

from src.Auteur import Auteur
from src.PieceJointe import PieceJointe
from src.Text import Text


class Message:
    def __init__(self, listRawContent:list, auteur:Auteur):
        _id, rawStrTimestamp, rawStrMessage, rawStrAttachments = listRawContent
        self.id = int(_id)
        self.dateTime = datetime.fromisoformat(rawStrTimestamp) + timedelta(hours=2)
        self.text = Text(rawStrMessage)
        self.attachments = self.getAttachments(rawStrAttachments)
        self.auteur = auteur
        self.y = None

    def __str__(self) -> str:
        result = " ".join([self.auteur.nom, self.dateToString(), "-->"])
        if self.isHaveText():
            return " ".join([result, self.text.rawString])
        return " ".join([result, "C'est vide"])

    @staticmethod
    def getAttachments(rawString: str):
        result = []
        if rawString:
            listAttachments = rawString.split(" ")
            for attachmentUrl in listAttachments:
                result.append(PieceJointe(attachmentUrl))
        return result

    def isHaveText(self)->bool:
        return bool(not self.text.isEmpty())

    def isHaveAttachment(self)->bool:
        return bool(self.attachments)

    def dateToString(self)->str:
        return self.dateTime.strftime("%d/%m/%Y %H:%M")

    def setY(self, y)->None:
        self.y = y