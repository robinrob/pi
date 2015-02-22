#!/usr/bin/env python

#!/usr/bin/env python

import sys, random
sys.path.append("/home/pi/mcpi/api/python/mcpi")
import minecraft



BACKGROUND_BLOCK = 155
FOREGROUND_BLOCK = 49

HEIGHT = 100
WIDTH = HEIGHT * 7 / 4

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


iterations = 1000
values = [][]



mc.setBlocks(-WIDTH / 2, 20, -HEIGHT / 2, WIDTH / 2, 20, HEIGHT /2, BACKGROUND_BLOCK)

for x in range(-WIDTH / 2, WIDTH / 2):
    for z in range(-HEIGHT / 2, HEIGHT / 2):
        #mc.setBlock(BACKGROUND_BLOCK)






class Complex:
    
    def __init__(self, real, imag):
        self.real = x
        self.image = y


    def square():
	self.x = self.x * self.x - self.y * self.y
	self.y = 2 * self.x * self.y
