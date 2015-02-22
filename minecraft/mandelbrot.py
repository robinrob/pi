#!/usr/bin/env python

import sys, random
sys.path.append("/home/pi/mcpi/api/python/mcpi")
import minecraft

from complex import Complex


BACKGROUND_BLOCK = 155
FOREGROUND_BLOCK = 49


GROUND=50

ITERATIONS=10
CONSTANT = Complex(1, 1)


scale = 100
resolution = 1.0 / scale

x_min = -2.5
x_max = 1
x_range = (x_max - x_min)

y_min = -1
y_max = 1
y_range = (y_max - y_min)

WIDTH = int(x_range * scale)
HEIGHT = int(y_range * scale)


mc = minecraft.Minecraft.create()
#mc.postToChat("Welcome to minecraft Maze!")

mc.setBlocks(-100, -100, -100, 100, 100, 100, 0)
mc.setBlocks(-5 / 7 * WIDTH, GROUND, -HEIGHT / 2, 2 / 7 * WIDTH, GROUND, HEIGHT / 2, BACKGROUND_BLOCK)

mc.player.setTilePos(0, GROUND+5, 0)

points = [[0] * HEIGHT] * WIDTH

for x in [resolution * x for x in range(int(x_min * scale), int(x_max +1 * scale))]:
    for y in [resolution * y for y in range(int(y_min * scale), int(y_max +1 * scale))]:
       square = x * x + y * y
       if square < 4:
            pass
            #mc.setBlock(int(x * scale), GROUND, int(y * scale), FOREGROUND_BLOCK)
