from os import path

from PIL import Image, ImageDraw

from src.Constants import *


class Auteur:
    def __init__(self, rawString: str):
        self.xDate = None
        self.PP = None
        self.masqueEllipse = None
        self.nom = rawString
        self.taillePP = 35
        self.load()

    def load(self) -> None:
        cheminFichier = path.join("data", "pp", self.nom) + ".png"

        dimensionEllipse = (0, 0, self.taillePP - 1, self.taillePP - 1)

        self.PP = Image.open(cheminFichier).resize((self.taillePP, self.taillePP))

        self.masqueEllipse = Image.new("L", self.PP.size)

        ImageDraw.Draw(self.masqueEllipse).ellipse(dimensionEllipse, fill=255)

        # On récupère la coordonnée x du nom de l'auteur pour afficher la date au bon emplacement
        calculateurCoordonee = ImageDraw.Draw(Image.new("RGB", (1, 1)))

        coordonneeBoiteNom = calculateurCoordonee.textbbox(
            (x_after_PP, 0),
            self.nom,
            **styles.get("auteur", "textbox")
        )
        self.xDate = coordonneeBoiteNom[2] + mar_left_date

    def __eq__(self, other):
        return self.nom == other
