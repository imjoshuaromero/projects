import qrcode

img = qrcode.make("https://imjoshuaromero.github.io/projects/")
img.save("her.png", "PNG")