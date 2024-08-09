# qr-vanity
<p>
  <img alt="example logo"src="example.png" align="left" width="110" height="110">
  <b>Automatically embedding pixel art in QR-codes.</b><br>
<br><br>←example output<p>

## Setup and usage:
- sudo apt install python3-dev python3-setuptools python3-pip libzbar0 libzbar-dev
- pip3 install -r requirements.txt

### Random position:

**usage:** ./qrvanity.py input.png "encoded message" all<br>
**output:** one or multiple output.png *might include center_fit.png*<br>
**input format:** pixel art as small black and white binary image (no grayscales)<br>

### Centered pixel art:

**usage:** ./qrvanity.py input.png "encoded message" center<br>
**output:** center_fit.png<br>
**input format:** pixel art as small black and white binary image (no grayscales)<br>

### Advice:
- Use transparent pixels where you don't care (outside the motive if it has non-rectangular borders). It will then occupy less data modules (QR-code pixels) and the resulting QR-code will be smaller.
- Drawing a white border around black motives will improve visibility, because it keeps black data modules away.
- The tool may often generate QR-codes that are not strictly valid according to specifications but can nevertheless be read by most QR-code readers.

## Python dependencies
- Pillow
- PyQRCode
- zbarlight
- pypng
