from PIL import Image, ImageDraw, ImageFont

image = Image.new("RGB", (400, 200), (49, 51, 56))
draw = ImageDraw.Draw(image)
font1 = ImageFont.truetype("../font/ggsans-Bold.ttf", 14)
font2 = ImageFont.truetype("../font/ggsans-Medium.ttf", 14)
font3 = ImageFont.truetype("../font/ggsans-Medium.ttf", 12)
red = (255, 0, 0)  # Rouge

x = 50
y = 60
text = "Gibus"
draw.text((x, y), text, font=font1, fill="white")

# Ajouter la chaîne "01/06/2019 13:15" à côté de la chaîne "Gibus"
bbox = draw.textbbox((0, 0), text, font=font1)
print(bbox)
x2 = bbox[2] + x + 10  # Ajouter un espace de 10 pixels entre les deux chaînes de texte
y2 = y+2
gray = (187, 187, 187)
text2 = "01/06/2019 13:15"
draw.text((x2, y2), text2, font=font3, fill=gray)

image.putpixel((x, y), red)

# petit = +4 10
# grand = +2 12

x = 50
y = 80
text = "du coup tu m'envoies les panorama?\ntest saut de ligne"
draw.text((x, y), text, font=font2, fill="white", spacing=8)

image.putpixel((x, y), red)

image.save("image_text.png")
image.show()
