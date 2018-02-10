<<<<<<< Updated upstream
#Tartan Hacks 2018



=======
try:
    import Image
except ImportError:
    from PIL import Image
>>>>>>> Stashed changes
import pytesseract


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
































