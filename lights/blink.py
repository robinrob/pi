#!/usr/bin/env python

import sys

from led import Led


pin = int(sys.argv[1])
freq = int(sys.argv[2])

Led(pin).blink(freq)
