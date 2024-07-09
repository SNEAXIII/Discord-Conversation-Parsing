from src.ElementMessage import ElementMessage


class PieceJointe(ElementMessage):
    def __init__(self, url: str):
        super().__init__(url)

    def show(self):
        print("Implémentation de la méthode abstraite")
