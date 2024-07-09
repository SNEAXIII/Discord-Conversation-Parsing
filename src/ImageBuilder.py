from PIL import Image
from PIL import ImageDraw

from src import Message, Couleur
from src.Styles import Styles

styles = Styles()
yDebut = 20
mar_top_PP = 10
pad_top_PP = 5
mar_left_date = 10
mar_top_p = 22
mag_top_end = yDebut
x_base_PP = 20
x_after_PP = 68


class ImageBuilder:
    def __init__(self):
        self.dessinImage = None
        self.image = None

    def calculerDimensionImage(self):
        # todo a faire
        pass

    def build(self, listeMessage: list[Message]):
        calculateurCoordonee = ImageDraw.Draw(Image.new("RGB", (1, 1)))
        yActuel = yDebut
        xMax = 0

        # On va calculer les coordonnées en ordonnée de l'emplacement des messages un par un
        for message in listeMessage:
            message.setY(yActuel)
            coordonneeBoiteTexte = calculateurCoordonee.textbbox(
                (0, yActuel),
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
        # self.image.show()

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

        # On récupère la coordonnée x pour afficher la date
        dessinImage.textbbox((x, y), auteur, **styles.get("auteur", "textbox"))