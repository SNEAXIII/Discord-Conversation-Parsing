from os import path
from src.Message import Message
from random import randint
from csv import reader
from src.Author import Author


class AllMessages:
    def __init__(self, listMember):
        self.listAuthor = self.getAllAuthors(listMember)
        self.listMessages = self.getAllMessagesFromCSV(self.listAuthor)

    def getAllAuthors(self, listMember):
        listAuthor = []
        for member in listMember:
            listAuthor.append(Author(member))
        return listAuthor

    def getAllMessagesFromCSV(self, listMember):
        listMessages = []
        for member in self.listAuthor:
            csvPath = path.join(".", "data", "csv", member.name) + ".csv"
            with open(csvPath, "r", encoding="utf-8") as csvfile:
                _reader = reader(csvfile)
                next(_reader)
                for row in _reader:
                    listMessages.append(Message(row, member))
        return sorted(listMessages, key=lambda x: x.id)
