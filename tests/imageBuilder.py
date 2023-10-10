from PIL import Image, ImageDraw, ImageFont

image = Image.new("RGB", (400, 200), (49, 51, 56))
draw = ImageDraw.Draw(image)
font1 = ImageFont.truetype("font/ggsans-Bold.ttf", 14)
font2 = ImageFont.truetype("font/ggsans-Medium.ttf", 14)
x = 50
y = 60
text = "Gibus"
draw.text((x, y), text, font=font1, fill="white")
x = 50
y = 80
text = "du coup tu m'envoies les panorama?"
draw.text((x, y), text, font=font2, fill="white")
image.save("image_text.png")
image.show()
