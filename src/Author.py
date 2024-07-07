from PIL import Image
from os import path


class Author:
    def __init__(self, rawString):
        self.name = rawString
        # TODO impelementer les images de pp au bon format
        _path = path.join("data", "pp", self.name)+".png"
        self.profilePicture = Image.open(f"{_path}")
        xBase = 20

    def __eq__(self, other):
        return self.name == other
