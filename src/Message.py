from datetime import datetime
from src.Text import Text
from src.Attachment import Attachment
from src.Author import Author


class Message:
    def __init__(self, listRawContent, strAuthorName):
        _id, rawStrTimestamp, rawStrMessage, rawStrAttachments = listRawContent
        self.id = int(_id)
        self.dateTime = datetime.fromisoformat(rawStrTimestamp)
        self.text = Text(rawStrMessage)
        self.attachments = self.getAttachments(rawStrAttachments)
        self.author = Author(strAuthorName)

    def __str__(self):
        result = self.author.name
        if self.isHaveText():
            return f"{result} --> {self.text.rawString}"
        return f"{result} --> C'est vide"

    def getAttachments(self, rawString):
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

    # TODO
    def show(self):
        pass
