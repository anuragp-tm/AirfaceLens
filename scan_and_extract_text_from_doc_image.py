import cv2
import numpy as np 
import os
from configobj import ConfigObj
try:
    config = ConfigObj('airface_config.ini')
    imgDir=config['IMAGE_DIR']
    imgName=config['IMAGE_NAME']
    imageFile=os.path.join(imgDir,imgName)
    

    img = cv2.imread(imageFile) # Read Image
    height, width, channels = img.shape # Find Height And Width Of Image

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # RGB To Gray Scale

    kernel = np.ones((5, 5), np.uint8) # Reduce Noise Of Image
    erosion = cv2.erode(gray, kernel, iterations=1)
    opening = cv2.morphologyEx(erosion, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)

    edges = cv2.Canny(closing, 20, 240) # Find Edges

    # Get Threshold Of Canny
    thresh = cv2.adaptiveThreshold(edges, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)  

    # Find Contours In Image
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)  

    # Find Biggest Contour
    areas = [cv2.contourArea(c) for c in contours]
    max_index = np.argmax(areas)
    print(max_index)

    # Find approxPoly Of Biggest Contour
    epsilon = 0.1 * cv2.arcLength(contours[max_index], True)
    approx = cv2.approxPolyDP(contours[max_index], epsilon, True)

    # Crop The Image To approxPoly
    pts1 = np.float32(approx)
    pts = np.float32([[0, 0], [width, 0], [width, height], [0, height]])
    matrix = cv2.getPerspectiveTransform(pts1, pts)
    result = cv2.warpPerspective(img, matrix, (width, height))

    flip = cv2.flip(result, 1) # Flip Image
    rotate = cv2.rotate(flip, cv2.ROTATE_90_COUNTERCLOCKWISE) # Rotate Image
    
    cv2.imshow('Result',rotate)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
except Exception as e:
    print(e)
