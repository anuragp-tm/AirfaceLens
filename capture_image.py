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
    ret,frame = cap.read()
   
    cv2.imwrite(imageFile,frame)
        
       
    return frame
    
take_photo()

