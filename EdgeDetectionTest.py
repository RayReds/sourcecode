from PIL import Image, ImageOps
import os
img = Image.open('Sample.jpg')
img = ImageOps.grayscale(img)
width, height = img.width, img.height
copy = img
#Add Gaussian Filter
GausFilter = [
[1, 4, 7, 4, 1],
[4, 16,26,16,4],
[7, 26,41,26,7],
[4, 16,26,16,4],
[1, 4, 7, 4, 1],
]
Coords = [
[[-2, -2], [-1, -2], [0, -2], [1, 2], [2, 2]],
[[-2, -1], [-1, -1], [0, -1], [1, 1], [1, 2]],
[[-2, 0], [-1, 0], [0, 0], [1, 0], [2, 0]],
[[-2, 1,], [-1, 1], [0, 1], [1, 1], [2, 1]],
[[-2, 2], [-1, 2], [0, 2], [1, 2], [2, 2]],
]
Values = 0
for x in range(2, width-2):
    for y in range(2, height-2):
        for cordX in range(5):
            for cordY in range(5):
                pos = Coords[cordY][cordX]
                X, Y = x+pos[0], y+pos[1]
                Mod = GausFilter[cordX][cordY]
                value = img.getpixel((X, Y))
                Values += value
    copy.putpixel((x,y),round(Values/25))
copy.show()
