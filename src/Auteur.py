from os import path

from PIL import Image, ImageDraw

from src.Constants import taillePP, mar_left_date, styles, x_after_PP


class Auteur:
    def __init__(self, nom: str):
        self.xDate = None
        self.PP = None
        self.masqueEllipse = None
        self.nom = nom
        self.load()

    def load(self) -> None:
        cheminFichier = path.join("data", "pp", self.nom) + ".png"

        dimensionEllipse = (0, 0, taillePP - 1, taillePP - 1)

        self.PP = Image.open(cheminFichier).resize((taillePP, taillePP))

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
