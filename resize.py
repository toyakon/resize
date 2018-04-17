import os
import sys
from PIL import Image

args = sys.argv[1:]

rs = int(args[args.index("-r") + 1]) if "-r" in args else 2
gr = args[args.index("-g") + 1] if "-g" in args else "r"
dn = args[args.index("-d") + 1] if "-d" in args else "resize"

files = os.listdir(os.getcwd())
if dn not in files:
    os.mkdir(dn)

imgs = [f for f in files if ".jpg" in f]

for im in imgs:
    img = Image.open(im)
    name, ext = os.path.splitext(im)
    width, height = img.size

    rimg = img.resize((width//rs, height//rs))
    rimg.save(f"./{dn}/{name}_{gr}{ext}", quality=75)
