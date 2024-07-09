from PIL import Image
from PIL import ImageDraw

from src import Message, Couleur, Auteur
from src.Constants import *
from src.Styles import Styles



class ImageBuilder:
    def __init__(self):
        self.dessinImage = None
        self.image = None
        self.calculateurCoordonee = ImageDraw.Draw(Image.new("RGB", (1, 1)))

    def calculerDimensionImage(self):
        # todo a faire
        pass

    def build(self, listeMessage: list[Message]):
        yActuel = yDebut
        xMax = 0

        # On va calculer les coordonnées en ordonnée de l'emplacement des messages un par un
        for message in listeMessage:
            message.setY(yActuel)
            coordonneeBoiteTexte = self.calculateurCoordonee.textbbox(
                (0, 0),
                message.text.show(),
                **styles.get("auteur", "textbox")
            )
            xMax = max(xMax, coordonneeBoiteTexte[2])
            yActuel += mar_top_PP + mar_top_p + coordonneeBoiteTexte[3]
        xMax += x_after_PP
        yActuel += mag_top_end

        # On construit l'image avec les bonnes dimensions
        # todo verifier que la marge du x soit pas trop élevée
        self.image = Image.new("RGB", (xMax, yActuel), Couleur.FOND)
        self.dessinImage = ImageDraw.Draw(self.image)

        # On parcourt tous les messages et on les ajoute à l'image finale
        for message in listeMessage:
            self.colleMessage(message)

        # On affiche le résultat final
        self.image.show()

    def colleMessage(self, message: Message):
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
            spacing=10
        )
