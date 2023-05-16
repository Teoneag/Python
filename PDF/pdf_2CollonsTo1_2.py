import fitz
import io
from PIL import Image
pdf_file = fitz.open("D:\Saguna\Math\A306.pdf")

imageList = [Image.open(io.BytesIO(pdf_file.extractImage(pdf_file[1].getImageList()[0][0])["image"]))]

for page_index in range(2, len(pdf_file)):
    print(page_index)
    image = Image.open(io.BytesIO(pdf_file.extractImage(pdf_file[page_index].getImageList()[0][0])["image"]))
    crop_img1 = image.crop((0, 0, image.size[0]/2, image.size[1])).convert('RGB')
    crop_img2 = image.crop((image.size[0]/2, 0, image.size[0], image.size[1])).convert('RGB')
    imageList.extend([crop_img1, crop_img2])
cover = Image.open("D:\Programming\Python\PDF\Cover.png").convert('RGB')
cover.save("Pdf_1.pdf", save_all = True, append_images = imageList)