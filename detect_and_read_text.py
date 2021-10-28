# read an image and extract text from the image
# import modules
import cv2
import pytesseract
import easyocr
import os
from configobj import ConfigObj
#import configparser
try:
    config = ConfigObj('airface_config.ini')
    imgDir=config['IMAGE_DIR']
    imgName=config['IMAGE_NAME']
    imageFile=os.path.join(imgDir,imgName)
    read_text_method=config['TEXT_READ_METHOD']
    #text_lang=config['TEXT_LANG']
    #text_lang=text_lang.split(',')
    #print(type(text_lang))
    #print(text_lang)
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
        text_lang=config['TEXT_LANG']
        reader = easyocr.Reader(text_lang)
        result = reader.readtext(img, detail=0)
        return result
    
    if read_text_method=='pytesseract':
        textOutput=read_text_from_image(imageFile)
    elif read_text_method=='easyocr':
        textOutput='\n' .join(read_easyocr_text(imageFile))
    #else:
        #textOutput=''
        #print("Unavailable option.Please choose either pytesseract or easyocr ")

    #textOutput=text if read_text_method=="pytesseract" else ' '.join(result)
    print(textOutput)
except Exception as e:
    print(f"Failed to read text from the image.{e}")