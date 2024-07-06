from PIL import ImageFont


class FontImportError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class WrongSelectedStyle(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class Styles:
    def __init__(self):
        self._disponible = {
            "auteur": ("ggsans", "bold", 14, "white"),
            "date": ("ggsans", "medium", 12, (174, 174, 174)),
            "message": ("ggsans", "medium", 14, "white")
        }

    def buildOne(self, nom: str, epaisseur: str, taille: int, couleur: str | tuple):
        cheminFont = f"../src/font/{nom}-{epaisseur}.ttf"

        try:
            trueType = ImageFont.truetype(cheminFont, taille)
        except OSError:
            raise FontImportError(f"La font suivante ne peut pas être importée\n --> {cheminFont}")

        return {"font": trueType, "fill": couleur}

    def get(self, fontDemande: str) -> dict:
        if fontDemande not in self._disponible.keys():
            raise WrongSelectedStyle(
                f"Le style demandé n'est pas valide !!!\n" +
                f"Style demandé --> {fontDemande}\n" +
                f"Fonts disponibles --> {', '.join(self._disponible)}"
            )

        return self.buildOne(*self._disponible[fontDemande])


test = Styles()
print(test.get("date"))
