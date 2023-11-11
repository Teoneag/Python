from PIL import Image
import os

path = os.getcwd() + "\Crop_all_img\Img"
dirs = os.listdir(path)

for item in dirs:
    fullpath = os.path.join(path, item)
    if os.path.isfile(fullpath):
        im = Image.open(fullpath)
        f, e = os.path.splitext(fullpath)
        width, height = im.size
        imCrop = im.crop((0, 0, width, 0.95 * height))
        imCrop.save(f + 'Cropped.jpg', "JPEG", quality=100)
