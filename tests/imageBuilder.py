from PIL import Image, ImageDraw, ImageFont

image = Image.new("RGB", (400, 200), (49, 51, 56))
draw = ImageDraw.Draw(image)
font1 = ImageFont.truetype("../font/ggsans-Bold.ttf", 14)
font2 = ImageFont.truetype("../font/ggsans-Medium.ttf", 14)
font3 = ImageFont.truetype("../font/ggsans-Medium.ttf", 12)
red = (255, 0, 0)  # Rouge

tupleTaillePP = (35, 35)
pp = Image.open("../data/pp/MisterBalise.webp").resize(tupleTaillePP)

masque = Image.new("RGBA", tupleTaillePP, (0, 0, 0, 0))
draw2 = ImageDraw.Draw(masque)
rayon = tupleTaillePP[0] // 2
centre = (tupleTaillePP[0] // 2, tupleTaillePP[1] // 2)
draw2.ellipse((centre[0] - rayon, centre[1] - rayon, centre[0] + rayon, centre[1] + rayon), fill=(0, 0, 0, 255))

ppCercle = Image.new("RGBA", tupleTaillePP)
ppCercle.paste(pp, mask=masque)

image.paste(ppCercle, (0, 0))

x = 50
y = 60
text = "MisterBalise"
draw.text((x, y), text, font=font1, fill="white")

bbox = draw.textbbox((0, 0), text, font=font1)
print(bbox)
x2 = bbox[2] + x + 10
y2 = y + 2
gray = (174, 174, 174)
text2 = "01/06/2019 13:15"
draw.text((x2, y2), text2, font=font3, fill=gray)

image.putpixel((x, y), red)

# petit = +4 10
# grand = +2 12

x = 50
y = 80
text = "tu va bien ou quoi ???"
draw.text((x, y), text, font=font2, fill="white", spacing=8)

image.putpixel((x, y), red)

image.save("image_text.png")
image.show()
