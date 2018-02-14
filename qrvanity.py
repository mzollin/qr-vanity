#!/usr/bin/env python3

# Copyright (c) 2018 Marco Zollinger
# Licensed under MIT, the license file shall be included in all copies

from PIL import Image
from io import BytesIO
import pyqrcode
import zbarlight
import sys

with open(sys.argv[1], 'rb') as input_file:
    input_image = Image.open(input_file)
    try:
        input_image.load()
    except (OSError, IOError) as e:
        print("Invalid image: {}".format(e))

    success = False
    # try versions 1 to 40, smaller first
    for version in range(1, 41):
        try:
            qr_object = pyqrcode.create(sys.argv[2], error='H', version=version)
        except ValueError:
            print("data payload too small (version {})".format(version))
            continue
        qr_file = BytesIO()
        # TODO: fix quiet zone overshoot problem
        qr_object.png(qr_file, quiet_zone=1)
        # TODO: error handling in case qr-code generation fails
        qr_image = Image.open(qr_file)
        qr_image.load()

        # try input image on every position on qr-code
        print("trying to fit in version {}".format(version))
        qr_width, qr_height = qr_image.size
        input_width, input_height = input_image.size
        for x in range(qr_width - input_width):
            for y in range(qr_height - input_height):
                #print("DEBUG: qrsize:{}, x:{}, y:{}".format(qr_width, x, y))
                output_image = qr_image.copy()
                output_image.paste(input_image, (x, y), input_image)

                # try to read the result as a qr-code and check
                try:
                    qr_readback = zbarlight.scan_codes('qrcode', output_image)
                except SyntaxError:
                    continue
                for qrcode in (qr_readback or []):
                    qrcode = qrcode.decode('ascii', errors='replace')
                    if qrcode == sys.argv[2]:
                        output_image = output_image.resize((4*qr_width, 4*qr_height), Image.LANCZOS)
                        output_image.save('output_{}_{}.png'.format(x, y))
                        success = True
        if success:
            print("fit found in version {}".format(version))
            sys.exit(0)
    print("sorry, no luck!")
