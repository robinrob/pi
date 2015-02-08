#!/usr/bin/env python

import sys

from led import Led


pin = int(sys.argv[1])

Led(pin).off()
