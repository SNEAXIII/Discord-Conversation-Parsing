from PIL import Image, ImageDraw, ImageFont
image = Image.new("RGB", (400, 200), (49, 51, 56))
dessinImage = ImageDraw.Draw(image)
font1 = ImageFont.truetype("../src/font/ggsans-Bold.ttf", 14)
font2 = ImageFont.truetype("../src/font/ggsans-Medium.ttf", 14)
font3 = ImageFont.truetype("../src/font/ggsans-Medium.ttf", 12)
red = (255, 0, 0)  # Rouge

imageLink = "../data/pp/MisterBalise.png"
taillePP = 35
tupleEllipseDimension = (0, 0, taillePP - 1, taillePP - 1)

PP = Image.open(imageLink).resize((taillePP, taillePP))

masqueEllipse = Image.new("L", PP.size)

ImageDraw.Draw(masqueEllipse).ellipse(tupleEllipseDimension, fill=255)

image.paste(PP, (20, 20), mask=masqueEllipse)

x = 60
y = 20
author = "MisterBalise"
dessinImage.text((x, y), author, font=font1, fill="white")

bbox = dessinImage.textbbox((0, 0), author, font=font1)
print(bbox)
x2 = bbox[2] + x + 10
y2 = y + 2
gray = (174, 174, 174)
date = "Aujourd’hui à 02:15"
dessinImage.text((x2, y2), date, font=font3, fill=gray)

image.putpixel((x, y), red)

# petit = +4 10
# grand = +2 12

x = 60
y = 50
text = "message de test8"
dessinImage.text((x, y), text, font=font2, fill="white")

image.putpixel((x, y), red)

image.save("image_text.png")
image.show()
