# read an image and extract text from the image
# import modules
import cv2
import pytesseract
import easyocr
import os
from detect_objects import inp

#==== text detection using pytesseract ====== #
def read_text_from_image(inp):
    # read an image
    img=cv2.imread(inp)
    #print(img.shape)
    # read text from the image
    text=pytesseract.image_to_string(img)
    return text

# ===== text detection using easyocr =====#
def read_easyocr_text(inp):
    reader = easyocr.Reader(['en'])
    result = reader.readtext('resources/images/quote3.jpeg', detail=0)
    return result
