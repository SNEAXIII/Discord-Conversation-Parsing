from PIL import Image, ImageDraw

from src.Styles import Styles

styles = Styles()

image = Image.new("RGB", (400, 400), (49, 51, 56))
image.resize((1000, 1000))

x = 68
y = 20

imageLink = "./data/pp/Gibus.png"
taillePP = 35
tupleEllipseDimension = (0, 0, taillePP - 1, taillePP - 1)

PP = Image.open(imageLink).resize((taillePP, taillePP))

masqueEllipse = Image.new("L", PP.size)

ImageDraw.Draw(masqueEllipse).ellipse(tupleEllipseDimension, fill=255)

image.paste(PP, (20, y + 5), mask=masqueEllipse)

dessinImage = ImageDraw.Draw(image)
auteur = "Gibus"
dessinImage.text((x, y), auteur, **styles.get("auteur", "text"))

bbox = dessinImage.textbbox((x, y), auteur, **styles.get("auteur", "textbox"))
date = "Aujourd’hui à 20:12"
dessinImage.text((bbox[2] + 10, y + 2), date, **styles.get("date", "text"))

y += 22
text = "Je me fais gueuler dessusparce que\n j'ai pas\n obéi😤"
dessinImage.text((x, y), text, **styles.get("message", "text"),spacing=10)
bbbb = dessinImage.textbbox((x, y), text, **styles.get("message", "textbox"),spacing=10)
dessinImage.rectangle(bbbb, outline="#0000ff")

y = bbbb[3] + 10

image.paste(PP, (20, y + 5), mask=masqueEllipse)

dessinImage = ImageDraw.Draw(image)
auteur = "Gibus"
dessinImage.text((x, y), auteur, **styles.get("auteur", "text"))

bbox = dessinImage.textbbox((x, y), auteur, **styles.get("auteur", "textbox"))
print(bbox)
x2 = bbox[2]+ 10
y2 = y + 2
date = "Aujourd’hui à 20:12"
dessinImage.text((x2, y2), date, **styles.get("date", "text"))

y += 22
text = "Je me fais gueuler dessusparce que\n j'ai pas\n obéi😤"
dessinImage.text((x, y), text, **styles.get("message", "text"),spacing=10)
bbbb = dessinImage.textbbox((0, 0), text, **styles.get("message", "textbox"),spacing=10)
newbb = tuple(coordRelative + coordAbsolue for coordRelative, coordAbsolue in zip(bbbb, (x, y) * 2))
print(f"{bbbb = }")
print(f"{newbb = }")
dessinImage.rectangle(newbb, outline="#0000ff")

image.save("image_text.png")
image.show()
