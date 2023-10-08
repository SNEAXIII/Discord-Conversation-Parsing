from datetime import datetime


class Message:
    def __init__(self, listRawContent, strAuthorName):
        _id, rawStrTimestamp, rawStrMessage, rawStrAttachments = listRawContent
        self.id = int(_id)
        self.dateTime = datetime.fromisoformat(rawStrTimestamp)
        # A implémenter
        # self.text = text(rawStrMessage)
        # A implémenter
        # self.attachement = attachement(rawStrAttachments)
        # A implémenter
        # self.author = author(strAuthorName)
