from PIL import Image
from PIL import ImageDraw

from src import Message, Couleur
from src.Constants import *


class ImageBuilder:
    def __init__(self):
        self.dessinImage = None
        self.image = None
        self.calculateurCoordonee = ImageDraw.Draw(Image.new("RGB", (1, 1)))

    def build(self, messages: list[Message], debug: bool = False) -> None:
        yActuel = yDebut
        xMax = 0

        # On va calculer les coordonnées en ordonnée de l'emplacement des messages un par un
        for message in messages:
            message.setY(yActuel)
            boiteTexte = self.calculateurCoordonee.textbbox(
                (0, 0),
                message.text.show(),
                **styles.get("message", "textbox"),
                spacing=multiLineSpacing
            )
            message.text.boiteTexte = boiteTexte
            xMax = max(xMax, boiteTexte[2])
            yActuel += mar_top_PP + mar_top_p + boiteTexte[3]

        # On construit l'image avec les bonnes dimensions
        xImage = xMax + x_after_PP * 2
        yImage = yActuel + mag_top_end

        self.image = Image.new("RGB", (xImage, yImage), Couleur.FOND)
        self.dessinImage = ImageDraw.Draw(self.image)

        # On parcourt tous les messages et on les ajoute à l'image finale
        for message in messages:
            self.colleMessage(message, debug=debug)

        # On affiche le résultat final
        self.image.show()

    def colleMessage(self, message: Message, debug: bool = False):
        # On colle la photo de profil de l'auteur
        auteur = message.auteur
        self.image.paste(auteur.PP, (x_base_PP, message.y + pad_top_PP), mask=auteur.masqueEllipse)

        # On colle le nom de l'auteur a coté de sa photo de profil
        self.dessinImage.text(
            (x_after_PP, message.y),
            auteur.nom,
            **styles.get("auteur", "text")
        )

        # On colle la date à côté de l'auteur du message
        self.dessinImage.text(
            (auteur.xDate, message.y + tra_top_date),
            message.dateToString(),
            **styles.get("date", "text")
        )

        # On finit par ajouter le texte du message
        self.dessinImage.text(
            (x_after_PP, message.y + mar_top_p),
            message.text.show(),
            **styles.get("message", "text"),
            spacing=multiLineSpacing
        )
        if debug:
            x1, y1, x2, y2 = message.text.boiteTexte
            self.dessinImage.rectangle(
                (
                    x1 + x_after_PP,
                    y1 + message.y + mar_top_p,
                    x2 + x_after_PP,
                    y2 + message.y + mar_top_p
                ),
                outline="#0000ff"
            )
