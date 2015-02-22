#!/usr/bin/env python

#!/usr/bin/env python

import sys, random
sys.path.append("/home/pi/mcpi/api/python/mcpi")
import minecraft

from complex import Complex


BACKGROUND_BLOCK = 155
FOREGROUND_BLOCK = 49

HEIGHT = 100
WIDTH = HEIGHT * 7 / 4

ITERATIONS=1000
CONSTANT=-1

mc = minecraft.Minecraft.create()
#mc.postToChat("Welcome to minecraft Maze!")
mc.player.setTilePos(0, 25, 0)

x_min = -2.5
x_max = 1
x_range = (x_max - x_min)
dx = x_range / WIDTH

y_min = -1
y_max = 1
y_range = (y_max - y_min)
dy = y_range / HEIGHT

mc.setBlocks(-WIDTH / 2, 20, -HEIGHT / 2, WIDTH / 2, 20, HEIGHT /2, BACKGROUND_BLOCK)


# Do the calculation
points = []
complex = Complex(0, 0);
print str(complex.x)
print str(complex.y)
points.append(complex)

for i in range(1, ITERATIONS):
    complex = Complex(complex.x - CONSTANT, complex.y).square()
    points.append(complex)



# Plot the points
for point in points:
    mc.setBlock(point.x, 20, point.y, FOREGROUND_BLOCK)


