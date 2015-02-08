#!/usr/bin/env python

from led import Led


pin = int(sys.argv[1])

Led(pin).off()
