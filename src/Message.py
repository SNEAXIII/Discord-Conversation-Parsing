from datetime import datetime
from src.Text import Text
from src.Attachment import Attachment


class Message:
    def __init__(self, listRawContent, strAuthorName):
        _id, rawStrTimestamp, rawStrMessage, rawStrAttachments = listRawContent
        self.id = int(_id)
        self.dateTime = datetime.fromisoformat(rawStrTimestamp)
        self.text = Text(rawStrMessage)
        # A implémenter
        # self.attachments = getAttachment(rawStrAttachments)
        # A implémenter
        # self.author = author(strAuthorName)

    def __str__(self):
        return self.text.rawstring

    def getAttachment(self, rawString):
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
