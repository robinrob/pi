#!/usr/bin/env python

import RPi.GPIO as GPIO
import time


class Led:

    def __init__(self, pin):
        self.pin = pin

        print "Using BOARD layout"
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)

        print "Setting pin " + str(self.pin) + " to OUT"
        GPIO.setup(self.pin, GPIO.OUT)


    def on(self):
        # print "Setting pin " + str(self.pin) + " to ON"
        GPIO.output(self.pin, True)


    def off(self):
        # print "Setting pin " + str(self.pin) + " to OFF"
        GPIO.output(self.pin, False)


    def blink(self, freq):
        print "Blinking at " + str(freq) + " times per second ..."
        while (True):
            self.on()
            time.sleep(1.0 / freq)
            self.off()
            time.sleep(1.0 / freq)
