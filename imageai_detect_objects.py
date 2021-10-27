#==== DECTECT AND REAR OBJECTS FROM AN IMAGE USING IMAGEAI ========#
# import libraries
from imageai.Detection import ObjectDetection
import os
from configobj import ConfigObj

# read airface config file 
config = ConfigObj('airface_config.ini')
imgDir=config['IMAGE_DIR'] # image directory
imgName=config['IMAGE_NAME'] # original image name
# object detected image name
odImgName=imgName.split('.')[0]+'_object_detected.'+imgName.split('.')[1]
originalImageFile=os.path.join(imgDir,imgName) # original image file path
odImageFile=os.path.join(imgDir,odImgName) # onbject detected image file path

detector=ObjectDetection()
execution_path = os.getcwd()

detector.setModelTypeAsRetinaNet()
detector.setModelPath( "resnet50_coco_best_v2.1.0.h5")
detector.loadModel()

detections = detector.detectObjectsFromImage(input_image=originalImageFile, output_image_path=odImageFile)

for eachObject in detections:
    print(eachObject["name"] , " : " , eachObject["percentage_probability"] )