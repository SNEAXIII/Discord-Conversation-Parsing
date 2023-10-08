from os import path
from src.Message import Message
from random import randint
from csv import reader


class AllMessages:
    def __init__(self, listMember):
        self.listMember = listMember
        self.listMessages = self.getAllMessagesFromCSV(self.listMember)
        # sorted(liste, key=lambda x: x[0])
        pass

    def getAllMessagesFromCSV(self, listMember):
        listMessages = []
        for member in self.listMember:
            csvPath = path.join(".", "data", "csv", member) + ".csv"
            with open(csvPath, "r", encoding="utf-8") as csvfile:
                _reader = reader(csvfile)
                next(_reader)
                for row in _reader:
                    listMessages.append(Message(row, member))
        return sorted(listMessages, key=lambda x: x.id)
