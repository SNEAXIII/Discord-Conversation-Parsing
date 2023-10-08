from os import path
import message
from random import randint


class AllMessages:
    def __init__(self, listMember):
        self.listMember = listMember
        self.listMessages = self.getAllMessagesFromCSV(self.listMember)
        # sorted(liste, key=lambda x: x[0])
        pass

    def getAllMessagesFromCSV(self, listMember):
        listMessages = []
        for member in self.listMember:
            csvPath = path.join("data", "csv", member)
            with open(csvPath, "r", encoding="utf-8") as csvfile:
                reader = reader(csvfile)
                next(reader)
                for row in reader:
                    message(row,member)
        # À fixer, car ce ne sera pas une liste, mais une liste d'ojet
        return sorted(listMessages, key=lambda x: x[0])
