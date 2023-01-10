import numpy as np
import math
import matplotlib.pyplot as plt
img = plt.imread('Sample.jpg',0)
filterX = [
[1, 2, 1],
[0, 0, 0],
[-1, -2, -1]
]
filterY = [
[1, 0, -1],
[2, 0, -2],
[1, 0, -1]
]
x, y, c = img.shape
vertical_edges = np.zeros_like(img)
for X in range(3, x-2):
    for Y in range(3, y-2):
        local = img[X-1:X+2, Y-1:Y+2, 0]
        current = local*filterX
        vertical = (current.sum()+10)//8
        current2 = local*filterY
        vertical2 = (current2.sum()+10)//8
        vertical_edges[X,Y] = math.sqrt((vertical**2)+(vertical2**2))*3
plt.imshow(vertical_edges)
plt.show()
