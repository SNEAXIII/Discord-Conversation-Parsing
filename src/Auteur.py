from os import path

from PIL import Image, ImageDraw


class Auteur:
    def __init__(self, rawString: str):
        self.PP = None
        self.masqueEllipse = None
        self.nom = rawString
        self.taillePP = 35
        self.xDate = None
        self.load()

    def load(self) -> None:
        cheminFichier = path.join("data", "pp", self.nom) + ".png"

        dimensionEllipse = (0, 0, self.taillePP - 1, self.taillePP - 1)

        self.PP = Image.open(cheminFichier).resize((self.taillePP, self.taillePP))

        self.masqueEllipse = Image.new("L", self.PP.size)

        ImageDraw.Draw(self.masqueEllipse).ellipse(dimensionEllipse, fill=255)

    def setXDate(self, x: int) -> None:
        self.xDate = x

    def __eq__(self, other):
        return self.nom == other
