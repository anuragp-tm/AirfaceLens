# ===== CAPTURE IMAGE FROM CAMERA ======#

import cv2
import os
from configobj import ConfigObj
#import configparser

config = ConfigObj('airface_config.ini')
imgDir=config['IMAGE_DIR']
imgName=config['IMAGE_NAME']
imageFile=os.path.join(imgDir,imgName)
# take photo from camera and save
def take_photo():
    cap = cv2.VideoCapture(0)
    while True:
        ret,frame = cap.read()
    
        #cv2.imwrite(imageFile,frame)
        cv2.imshow("Image",frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            cap.release()
            return frame
    
def save_image(img):
    status=cv2.imwrite(imageFile,img)
    if status :
        print("Image file saved.")
        
    
imgFrame=take_photo()
save_image(imgFrame)
cv2.waitKey(0)
cv2.destroyWindow()

