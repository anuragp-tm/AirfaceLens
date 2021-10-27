import cv2
import matplotlib.pyplot as plt
import os
from configobj import ConfigObj


config = ConfigObj('airface_config.ini')
imgDir=config['IMAGE_DIR']
imgName=config['IMAGE_NAME']
imageFile=os.path.join(imgDir,imgName)
image = cv2.imread(imageFile)
image=cv2.resize(image,(600,400),interpolation=cv2.INTER_AREA)  
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
# create a binary thresholded image
_, binary = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)
# show it
#plt.imshow(binary, cmap="gray")
#plt.show()
# find the contours from the thresholded image
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# draw all contours
image = cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
# show the image with the drawn contours
plt.imshow(image)
plt.show()