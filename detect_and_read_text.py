# read an image and extract text from the image
# import modules
import cv2
import pytesseract
import easyocr
import os
from configobj import ConfigObj
#import configparser

config = ConfigObj('airface_config.ini')
imgDir=config['IMAGE_DIR']
imgName=config['IMAGE_NAME']
imageFile=os.path.join(imgDir,imgName)
read_text_method=config['TEXT_READ_METHOD']


#==== text detection using pytesseract ====== #
def read_text_from_image(img):
    # read an image
    image=cv2.imread(img)
    #print(img.shape)
    # read text from the image
    text=pytesseract.image_to_string(image)
    return text

# ===== text detection using easyocr =====#
def read_easyocr_text(img):
    reader = easyocr.Reader(['en'])
    result = reader.readtext(img, detail=0)
    return result

text=read_text_from_image(imageFile)
result=read_easyocr_text(imageFile)

textOutput=text if read_text_method=="pytesseract" else ' '.join(result)
print(textOutput)