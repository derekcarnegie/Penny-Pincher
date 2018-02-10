#Tartan Hacks 2018



import pytesseract
from PIL import Image, ImageEnhance, ImageFilter


print ("Initializing fsociety...")
im = Image.open("TestCase.jpg") 
im = im.filter(ImageFilter.MedianFilter())
enhancer = ImageEnhance.Contrast(im)
im = enhancer.enhance(2)
im = im.convert('1')
im.save('temp2.jpg')

tessdata_dir_config = "C:\Program Files (x86)\Tesseract-OCR\tessdata"

text = pytesseract.image_to_string(Image.open('temp2.jpg'),config = tessdata_dir_config)
print(text.encode("utf8"))

print ("hello")
































