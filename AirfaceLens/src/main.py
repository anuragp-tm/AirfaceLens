# read an image and extract text from the image
# import modules
import cv2
import pytesseract
import easyocr
from fpdf import FPDF
import os

#==== text detection using pytesseract ====== #
# read an image
img=cv2.imread('resources/images/quote3.jpeg')
print(img.shape)
# read text from the image
text=pytesseract.image_to_string(img)
print(text)

# ===== text detection using easyocr =====#
reader = easyocr.Reader(['en'])
result = reader.readtext('resources/images/quote3.jpeg', detail=0)
print(result)
target_file_path='resources/templates/txt/image_text.txt'
target_pdf_dir='resources/templates/pdf'
with open(target_file_path, "w+") as f:
    for text in result :
        f.write(text + "\n")


# save FPDF() class into
# a variable pdf
pdf = FPDF()

# Add a page
pdf.add_page()

# set style and size of font
# that you want in the pdf
pdf.set_font("Arial", size=15)




# insert the texts in pdf
with open(target_file_path, "r") as f:
 for x in f:
    pdf.cell(200, 10, txt=x, ln=1, align='C')

# save the pdf with name .pdf
pdf.output(os.path.join(target_pdf_dir,'image_text.pdf'))
f.close()
"""
# preprocessing
# gray scale
def gray(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(r"/resource/images/img_gray.png", img)
    return img


# blur
def blur(img):
    img_blur = cv2.GaussianBlur(img, (5, 5), 0)
    cv2.imwrite(r"/resources/images//img_blur.png", img)
    return img_blur


# threshold
def threshold(img):
    # pixels with value below 100 are turned black (0) and those with higher value are turned white (255)
    img = cv2.threshold(img, 100, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY)[1]
    cv2.imwrite(r"/resources/images/img_threshold.png", img)
    return img

# Finding contours
im_gray = gray(im)
im_blur = blur(im_gray)
im_thresh = threshold(im_blur)

contours, _ = cv2.findContours(im_thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)


# text detection
def contours_text(orig, img, contours):
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)

        # Drawing a rectangle on copied image
        rect = cv2.rectangle(orig, (x, y), (x + w, y + h), (0, 255, 255), 2)

        cv2.imshow('cnt', rect)
        cv2.waitKey()

        # Cropping the text block for giving input to OCR
        cropped = orig[y:y + h, x:x + w]

        # Apply OCR on the cropped image
        config = ('-l eng --oem 1 --psm 3')
        text = pytesseract.image_to_string(cropped, config=config)

        print(text)"""