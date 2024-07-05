from PIL import Image, ImageDraw, ImageFont

image = Image.new("RGB", (400, 200), (49, 51, 56))
dessinImage = ImageDraw.Draw(image)
font1 = ImageFont.truetype("../font/ggsans-Bold.ttf", 14)
font2 = ImageFont.truetype("../font/ggsans-Medium.ttf", 14)
font3 = ImageFont.truetype("../font/ggsans-Medium.ttf", 12)
red = (255, 0, 0)  # Rouge

imageLink = "../data/pp/MisterBalise.webp"
taillephotoProfil = 35
rayon = taillephotoProfil // 2

photoProfil = Image.open(imageLink).resize((taillephotoProfil,taillephotoProfil))

tupleTaillephotoProfil = photoProfil.size

masque = Image.new("RGBA", tupleTaillephotoProfil, (0, 0, 0, 0))
dessinMasque = ImageDraw.Draw(masque)
centre = (rayon, rayon)
dessinMasque.ellipse((0,0,taillephotoProfil,taillephotoProfil), fill=(0, 0, 0, 255))
ppCercle = Image.new("RGBA", tupleTaillephotoProfil)
masque.show()
masque.putalpha(0)
ppCercle.paste(photoProfil, mask=masque)

image.paste(ppCercle, (0, 0))

x = 50
y = 60
author = "MisterBalise"
dessinImage.text((x, y), author, font=font1, fill="white")

bbox = dessinImage.textbbox((0, 0), author, font=font1)
print(bbox)
x2 = bbox[2] + x + 10
y2 = y + 2
gray = (174, 174, 174)
date = "01/06/2019 13:15"
dessinImage.text((x2, y2), date, font=font3, fill=gray)

image.putpixel((x, y), red)

# petit = +4 10
# grand = +2 12

x = 50
y = 80
text = "message de test"
dessinImage.text((x, y), text, font=font2, fill="white", spacing=8)

image.putpixel((x, y), red)

image.save("image_text.png")
image.show()
