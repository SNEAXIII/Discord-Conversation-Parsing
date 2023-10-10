from datetime import datetime
from src.Text import Text
from src.Attachment import Attachment
from src.Author import Author


class Message:
    def __init__(self, listRawContent, author):
        _id, rawStrTimestamp, rawStrMessage, rawStrAttachments = listRawContent
        self.id = int(_id)
        self.dateTime = datetime.fromisoformat(rawStrTimestamp)
        self.text = Text(rawStrMessage)
        self.attachments = self.getAttachments(rawStrAttachments)
        self.author = author

    def __str__(self):
        result = " ".join([self.author.name, self.dateToString(), "-->"])
        if self.isHaveText():
            return " ".join([result,self.text.rawString])
        return " ".join([result, "C'est vide"])

    @staticmethod
    def getAttachments(rawString):
        result = []
        if rawString:
            listAttachments = rawString.split(" ")
            for attachmentUrl in listAttachments:
                result.append(Attachment(attachmentUrl))
        return result

    def isHaveText(self):
        return bool(not self.text.isEmpty())

    def isHaveAttachment(self):
        return bool(self.attachments)

    def dateToString(self):
        return self.dateTime.strftime("%d/%m/%Y %H:%M")

    # TODO
    def show(self):
        pass
