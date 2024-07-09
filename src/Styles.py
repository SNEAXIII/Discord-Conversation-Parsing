from PIL import ImageFont

from src import Couleur


class FontImportError(Exception): pass


class WrongSelectedStyle(Exception): pass


class WrongSelectedMode(Exception): pass


class Styles:
    def __init__(self):
        self._disponible = {
            "auteur": ("ggsans", "bold", 14, Couleur.AUTEUR),
            "date": ("ggsans", "medium", 12, Couleur.DATE),
            "message": ("ggsans", "medium", 14, Couleur.MESSAGE)
        }
        self.charge = {elems[0]: self.buildOne(*elems[1]) for elems in self._disponible.items()}

    def buildOne(self, nom: str, epaisseur: str, taille: int, couleur: str | tuple):
        cheminFont = f"./src/font/{nom}-{epaisseur}.ttf"

        try:
            trueType = ImageFont.truetype(cheminFont, taille)
        except OSError:
            raise FontImportError(f"La font suivante ne peut pas être importée\n --> {cheminFont}")

        return {"text": {"font": trueType, "fill": couleur}, "textbox": {"font": trueType}}

    def get(self, fontDemande: str, modeDemande: str) -> dict:
        if fontDemande not in self._disponible:
            raise WrongSelectedStyle(
                "Le style demandé n'est pas valide !!!\n" +
                f"Style demandé --> {fontDemande}\n" +
                f"Fonts disponibles --> {', '.join(self._disponible)}"
            )

        if modeDemande not in self.charge[fontDemande]:
            raise WrongSelectedMode(
                "Le mode demandé n'est pas valide !!!\n" +
                f"Mode demandé --> {modeDemande}\n" +
                f"Fonts disponibles --> {', '.join(self.charge[fontDemande])}"
            )

        return self.charge[fontDemande][modeDemande]
