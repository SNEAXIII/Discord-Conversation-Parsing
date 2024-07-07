from PIL import Image, ImageDraw

from src.Styles import Styles

styles = Styles()

image = Image.new("RGB", (400, 200), (49, 51, 56))
dessinImage = ImageDraw.Draw(image)
# red = (255, 0, 0)

x = 68
y = 20

imageLink = "./data/pp/Gibus.png"
taillePP = 35
tupleEllipseDimension = (0, 0, taillePP - 1, taillePP - 1)

PP = Image.open(imageLink).resize((taillePP, taillePP))

masqueEllipse = Image.new("L", PP.size)

ImageDraw.Draw(masqueEllipse).ellipse(tupleEllipseDimension, fill=255)

image.paste(PP, (20, y+5), mask=masqueEllipse)


auteur = "Gibus"
dessinImage.text((x, y), auteur, **styles.get("auteur", "text"))

bbox = dessinImage.textbbox((0, 0), auteur, **styles.get("auteur", "textbox"))
print(bbox)
x2 = bbox[2] + x + 10
y2 = y + 2
date = "Aujourd’hui à 20:12"
dessinImage.text((x2, y2), date, **styles.get("date", "text"))

# image.putpixel((x, y), red)

# petit = +4 10
# grand = +2 12

y += 22
text = "Je me fais gueuler dessusparce que j'ai pas obéi😤"
dessinImage.text((x, y), text, **styles.get("message", "text"))

# image.putpixel((x, y), red)

image.save("image_text.png")
image.show()
