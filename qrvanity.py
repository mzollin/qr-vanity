#!/usr/bin/env python3

# Copyright (c) 2018 Marco Zollinger
# Licensed under MIT, the license file shall be included in all copies

import pyqrcode

qr = pyqrcode.create("testcode")
qr.png("qr_test.png", scale=6)
