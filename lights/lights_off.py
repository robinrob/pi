#!/usr/bin/env python

import RPi.GPIO as GPIO
import sys


pin = int(sys.argv[1])

print "Using BOARD layout"
GPIO.setmode(GPIO.BOARD)

print "Setting pin " + pin + " to OUT"
GPIO.setup(pin, GPIO.OUT)

print "Setting pin " + pin + " to ON"
GPIO.output(pin, False)

GPIO.cleanup()
