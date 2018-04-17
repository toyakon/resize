import os
import cv2
import numpy as np

files = os.listdir(os.getcwd())
if "resize" not in files:
    os.mkdir("resize")

imgs = [f for f in files if ".jpg" in f]

for im in imgs:
    img = cv2.imread(im)
    height, width = img.shape[:2]

    rimg = cv2.resize(img, (width//2, height//2))
    cv2.imwrite(f"./resize/r_{im}", rimg)