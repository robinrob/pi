#!/usr/bin/env python

import sys, random
sys.path.append("/home/pi/mcpi/api/python/mcpi")
import minecraft

from complex import Complex


BACKGROUND_BLOCK = 155
FOREGROUND_BLOCK = 49

HEIGHT = 100
WIDTH = HEIGHT * 7 / 4

ITERATIONS=10
CONSTANT = Complex(1, 1)

mc = minecraft.Minecraft.create()
#mc.postToChat("Welcome to minecraft Maze!")
mc.player.setTilePos(WIDTH / 2, 10, HEIGHT / 2)

x_min = -2.5
x_max = 1
x_range = (x_max - x_min)
dx = x_range / WIDTH

y_min = -1
y_max = 1
y_range = (y_max - y_min)
dy = y_range / HEIGHT

# mc.setBlocks(-WIDTH / 2, 20, -HEIGHT / 2, WIDTH / 2, 20, HEIGHT /2, BACKGROUND_BLOCK)


points = [[0] * WIDTH] * WIDTH

for x in [0.1 * x for x in range(int(x_min * 10), int(x_max +1 * 10))]:
    for y in [0.1 * y for y in range(int(y_min * 10), int(y_max +1 * 10))]:
       square = x * x - y * x + 2 * x * y 
       if square < 4:
           mc.setBlock(int(x * WIDTH), GROUND, int(y * HEIGHT), FOREGROUND_BLOCK)
