from PIL import Image, ImageOps
import os
img = Image.open('Sample.jpg')
img = ImageOps.grayscale(img)
width, height = img.width, img.height
copy = img
gxX = [
[1, 2, 1],
[0, 0, 0],
[-1, -2, -1]
]
gxY = [
[1, 0, -1],
[2, 0, -2],
[1, 0, -1]
]
cords = [
[[-1, -1], [0, -1], [0, -1]],
[[-1, 0], [0, 0], [1, 0]],
[[-1, 1], [0, 1], [1, 1]],
]
#Caltulating X edges
for x in range(1, width-1):
    for y in range(1, height-1):
        value = 0
        for cordX in range(3):
            for cordY in range(3):
                pos = cords[cordY][cordX]
                value += img.getpixel((x+pos[0],y+pos[1]))*gxX[cordX][cordY]
        copy.putpixel((x, y), value)
for x in range(1, width-1):
    for y in range(1, height-1):
        value = 0
        for cordX in range(3):
            for cordY in range(3):
                pos = cords[cordY][cordX]
                value += img.getpixel((x+pos[0],y+pos[1]))*gxY[cordX][cordY]
        copy.putpixel((x, y), value)
copy.show()
