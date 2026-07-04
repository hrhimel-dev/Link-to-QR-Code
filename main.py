# chang the url-test on your own way, thats why you will get the right code of that location.
# Remember to install the pyqrcode library if you haven't already. You can do this using pip:
# pip install pyqrcode pypng
# 
import pyqrcode
from pyqrcode import QRCode
from PIL import Image

# Folder where you want everything saved
save_dir = "/home/hrh/Downloads/"

# Text of URL to encode
url_text = "https://bigthink.com/neuropsych/assholes-psychology/"

# create the qrcode
qr = pyqrcode.create(url_text)

# Save as SVG file
# qr.svg(save_dir + "example_qrcode.svg", scale=8)

# save as PNG file
qr.png(save_dir + "asshole_qrcode.png", scale=6)

# ---- Extra setup: convert PNG to PDF ----
# img = Image.open(save_dir + "asshole_qrcode.png")
# img = img.convert("RGB")  # PDF format requires RGB, not RGBA
# img.save(save_dir + "asshole_qrcode.pdf")

print(f"Done! Files saved in {save_dir}")