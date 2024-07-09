from csv import reader
from os import path

from src.Auteur import Auteur
from src.Message import Message


class AllMessages:
    def __init__(self, listMember):
        self.listAuteur = self.getAllAuteurs(listMember)
        self.reset()

    def getAllAuteurs(self, listMember: list) -> list:
        listAuteur = []
        for member in listMember:
            listAuteur.append(Auteur(member))
        return listAuteur

    def getAllMessagesFromCSV(self):
        listMessages = []
        for member in self.listAuteur:
            csvPath = path.join(".", "data", "csv", member.nom) + ".csv"
            with open(csvPath, encoding="utf-8") as csvfile:
                _reader = reader(csvfile)
                next(_reader)
                for row in _reader:
                    listMessages.append(Message(row, member))
        return self.sortMessagesByDate(listMessages)

    def parseMessage(self, listMessages: list[Message]) -> list[Message]:
        nouvelleListe = []
        dernierAuteur = None
        for messageActuel in listMessages:
            auteurActuel = messageActuel.auteur
            if dernierAuteur == auteurActuel:
                nouvelleListe[-1].text.rawString += f"\n{messageActuel.text.rawString}"
            else:
                nouvelleListe.append(messageActuel)
            dernierAuteur = auteurActuel
            # todo ajouter les wrap des mots
        return nouvelleListe

    @staticmethod
    def sortMessagesByDate(listMessages: list) -> list:
        return sorted(listMessages, key=lambda x: x.id)

    def reset(self):
        self.listMessages = self.getAllMessagesFromCSV()
