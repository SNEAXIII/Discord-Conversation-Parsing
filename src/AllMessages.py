from csv import reader
from os import path

from src.Auteur import Auteur
from src.Message import Message


class AllMessages:
    listAuteur: list[Auteur]
    messages: list[Message]

    def __init__(self, members: list[str]):
        self.messages = None
        self.listAuteur = self.getAllAuteurs(members)
        self.reset()

    def getAllAuteurs(self, members: list[str]) -> list[Auteur]:
        listAuteur = []
        for member in members:
            listAuteur.append(Auteur(member))
        return listAuteur

    def getAllMessagesFromCSV(self) -> list[Message]:
        messages = []
        for member in self.listAuteur:
            csvPath = path.join(".", "data", "csv", member.nom) + ".csv"
            with open(csvPath, encoding="utf-8") as csvfile:
                _reader = reader(csvfile)
                next(_reader)
                for row in _reader:
                    messages.append(Message(row, member))
        return self.sortMessagesByDate(messages)

    def parseMessage(self, messages: list[Message]) -> list[Message]:
        nouvelleListe = []
        dernierAuteur = None
        for messageActuel in messages:
            auteurActuel = messageActuel.auteur
            if dernierAuteur == auteurActuel:
                nouvelleListe[-1].text.rawString += f"\n{messageActuel.text.rawString}"
            else:
                nouvelleListe.append(messageActuel)
            dernierAuteur = auteurActuel
            # todo ajouter les wrap des mots
        return nouvelleListe

    def getIdMessagesQuiContiennentTexte(self, echantillons: list[str]) -> list[int]:
        return [idMessage for idMessage, message in enumerate(self.messages) if message.siContient(echantillons)]

    def getMessagesParId(self, ids: list[int]) -> list[Message]:
        return [self.messages[idMessage] for idMessage in ids]

    def afficheMessagesQuiContiennentTexte(self, echantillons: list[str], marge: int = 0) -> None:
        idsSelectionnes = self.getIdMessagesQuiContiennentTexte(echantillons)
        nombreMessages = len(self.messages)
        for numeroPartie, idSelectionne in enumerate(idsSelectionnes):
            valeurMini = max(0, idSelectionne - marge)
            valeurMaxi = min(idSelectionne + marge, nombreMessages)
            messagesAParcourir = self.messages[valeurMini:valeurMaxi + 1]
            print(f"Partie de message numéro {numeroPartie + 1}:\n")
            for idMessageParcourus,message in enumerate(messagesAParcourir):
                print(f"Message numéro {idMessageParcourus + valeurMini} --> {message}")
            print()

    @staticmethod
    def sortMessagesByDate(messages: list[Message]) -> list[Message]:
        return sorted(messages, key=lambda x: x.id)

    def reset(self) -> None:
        self.messages = self.getAllMessagesFromCSV()
