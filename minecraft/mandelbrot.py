#!/usr/bin/env python

#!/usr/bin/env python

import sys, random
sys.path.append("/home/pi/mcpi/api/python/mcpi")
import minecraft



BACKGROUND_BLOCK = 155
FOREGROUND_BLOCK = 49

WIDTH = 100
HEIGHT = 100

mc = minecraft.Minecraft.create()
#mc.postToChat("Welcome to minecraft Maze!")
mc.player.setTilePos(0, 20, 0)

x_min = -2.5
x_max = 1
x_range = (x_max - xmin)
dx = x_range / WIDTH

y_min = -1
y_max = 1
y_range = (y_max - y_min)
dy = y_range / HEIGHT


for x in range(-WIDTH / 2, WIDTH / 2):
    for z in range(-HEIGHT / 2, HEIGHT / 2):
        mc.setBlock(BACKGROUND_BLOCK)


# for x in range(-WIDTH / 2, WIDTH / 2):
#     for z in range(-HEIGHT / 2, HEIGHT / 2):
#         mc.setBlock(BACKGROUND_BLOCK)
