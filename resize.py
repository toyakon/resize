import os
from PIL import Image

files = os.listdir(os.getcwd())
if "resize" not in files:
    os.mkdir("resize")

imgs = [f for f in files if ".jpg" in f]

for im in imgs:
    img = Image.open(im)

    width, height = img.size

    rimg = img.resize((width//2, height//2))
    rimg.save(f"./resize/r_{im}", quality=100, optimaize=True)
