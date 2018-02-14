# qr-vanity
Automatically embedding pixel art in QR-codes.

## Setup and usage:
- sudo apt install python3-dev python3-setuptools python3-pip libzbar0 libzbar-dev
- pip3 install -r requirements.txt

**usage:** ./qrvanity.py input.png "encoded message"<br>
**output:** output.png<br>
**input format:** Small black and white binary image (no grayscales)<br>
**advice:** Use transparent pixels where you don't care (outside the main motive if it has non-rectangular borders). It will then occupy less data modules (QR-code pixels) and the resulting QR-code will be smaller. Drawing a white border around black motives will improve visibility, because it keeps black data modules away.

## Python dependencies
- Pillow
- PyQRCode
- zbarlight
- pypng
