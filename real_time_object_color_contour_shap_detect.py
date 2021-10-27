import cv2
import numpy as np
import os
from configobj import ConfigObj

config = ConfigObj('airface_config.ini')
imageDir=config['IMAGE_DIR']
imageName=config['IMAGE_NAME']
imageFile=os.path.join(imageDir,imageName)
image = cv2.imread(imageFile)
image=cv2.resize(image,(600,400),interpolation=cv2.INTER_AREA)  
hsvImage = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# red color
low_red = np.array([161, 155, 84])
high_red = np.array([179, 255, 255])
red_mask = cv2.inRange(hsvImage, low_red, high_red)
kernel = np.ones((5, 5), np.uint8)
red_mask = cv2.erode(red_mask, kernel)
red = cv2.bitwise_and(image, image, mask=red_mask)

# Blue color
low_blue = np.array([94, 80, 2])
high_blue = np.array([126, 255, 255])
blue_mask = cv2.inRange(hsvImage, low_blue, high_blue)
kernel = np.ones((5, 5), np.uint8)
blue_mask = cv2.erode(blue_mask, kernel)
blue = cv2.bitwise_and(image, image, mask=blue_mask)
    
# Green color
low_green = np.array([25, 52, 72])
high_green = np.array([102, 255, 255])
green_mask = cv2.inRange(hsvImage, low_green, high_green)
kernel = np.ones((5, 5), np.uint8)
green_mask = cv2.erode(green_mask, kernel)
green = cv2.bitwise_and(image, image, mask=green_mask)
    
# Every color except white
low = np.array([0, 42, 0])
high = np.array([179, 255, 255])
mask = cv2.inRange(hsvImage, low, high)
kernel = np.ones((5, 5), np.uint8)
mask = cv2.erode(mask, kernel)
result = cv2.bitwise_and(image, image, mask=mask)

contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for contour in contours :
  area = cv2.contourArea(contour)
  approx = cv2.approxPolyDP(contour, 0.02*cv2.arcLength(contour, True), True)
  x = approx.ravel()[0]
  y = approx.ravel()[1]
  if len(approx) == 3:
        cv2.putText(image, 'Triangle', (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,0,0), 2)
  
  elif len(approx) == 4:
        cv2.putText(image, 'Quadrilateral', (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
  
  elif len(approx) == 5:
        cv2.putText(image, 'Pentagon', (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
  
  elif len(approx) == 6:
        cv2.putText(image, 'Hexagon', (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
  
  else:
        cv2.putText(image, 'circle', (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
cv2.imshow("image", image)
cv2.imshow("Red", red)
cv2.imshow("Blue", blue)
cv2.imshow("Green", green)
cv2.imshow("Result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()