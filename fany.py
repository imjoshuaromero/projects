import qrcode

img = qrcode.make("jas.jpg")
img.save("jas.png", "PNG")