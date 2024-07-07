from csv import reader
from os import path

from src.Author import Author
from src.Message import Message


class AllMessages:
    def __init__(self, listMember):
        self.listAuthor = self.getAllAuthors(listMember)
        self.listMessages = self.getAllMessagesFromCSV()

    def getAllAuthors(self, listMember: list) -> list:
        listAuthor = []
        for member in listMember:
            listAuthor.append(Author(member))
        return listAuthor

    def getAllMessagesFromCSV(self):
        listMessages = []
        for member in self.listAuthor:
            csvPath = path.join(".", "data", "csv", member.name) + ".csv"
            with open(csvPath, "r", encoding="utf-8") as csvfile:
                _reader = reader(csvfile)
                next(_reader)
                for row in _reader:
                    listMessages.append(Message(row, member))
        return self.sortMessagesByDate(listMessages)

    @staticmethod
    def sortMessagesByDate(listMessages: list) -> list:
        return sorted(listMessages, key=lambda x: x.id)
