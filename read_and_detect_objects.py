
import tensorflow as tf

import cv2
import os

import tensorflow_hub as hub
import pandas as pd
from configobj import ConfigObj

config = ConfigObj('airface_config.ini')
imgDir=config['IMAGE_DIR']
imgName=config['IMAGE_NAME']
imageFile=os.path.join(imgDir,imgName)
csvDir=config['CSV_DIR']
os.environ['CUDA_VISIBLE_DEVICES'] ="-1"

# read and resize to respect the input_shape

width = 600
height = 400
img=cv2.imread(imageFile)
inp = cv2.resize(img, (width , height ))

#Convert img to RGB
rgb = cv2.cvtColor(inp, cv2.COLOR_BGR2RGB)
# Converting to uint 8
rgb_tensor = tf.convert_to_tensor(rgb, dtype=tf.uint8)

#Add dims to rgb_tensor
rgb_tensor = tf.expand_dims(rgb_tensor , 0)

#we can load the model and the labels

# Loading model directly from TensorFlow Hub
detector = hub.load("https://tfhub.dev/tensorflow/efficientdet/lite2/detection/1")


# Loading csv with labels of classes
labels = pd.read_csv(os.path.join(csvDir,'labels.csv'), sep=';', index_col='ID')
labels = labels['OBJECT (2017 REL.)']

#we can create the predictions and put in the image the boxes and labels found:
# Creating prediction
boxes, scores, classes, num_detections = detector(rgb_tensor)

# Processing outputs
pred_labels = classes.numpy().astype('int')[0]
pred_labels = [labels[i] for i in pred_labels]
pred_boxes = boxes.numpy()[0].astype('int')
pred_scores = scores.numpy()[0]

# Putting the boxes and labels on the image
for score, ( ymin,xmin,ymax,xmax), label in zip(pred_scores, pred_boxes, pred_labels):
    if score < 0.5:
        continue
    print("inside for")
    score_txt = f'{100 * round(score)}%'
    img_boxes = cv2.rectangle(rgb,(xmin, ymax),(xmax, ymin),(0,255,0),2)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img_boxes, label,(xmin, ymax-10), font, 1.5, (255,0,0), 2, cv2.LINE_AA)
    cv2.putText(img_boxes,score_txt,(xmax, ymax-10), font, 1.5, (255,0,0), 2, cv2.LINE_AA)
    cv2.imshow("Image",img_boxes)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



