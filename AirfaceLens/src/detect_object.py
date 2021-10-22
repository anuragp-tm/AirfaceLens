# read a captured image and detect and classify the objects in the image =====
#===import modules====#
import tensorflow_hub as hub
import cv2
import numpy
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt

#====load and process image======#
width = 1028
height = 1028

# Load image by Opencv2
img = cv2.imread('resources/images/image.jpeg')
# Resize to respect the input_shape
inp = cv2.resize(img, (width , height ))

# Convert img to RGB
rgb = cv2.cvtColor(inp, cv2.COLOR_BGR2RGB)

# Converting to uint8
rgb_tensor = tf.convert_to_tensor(rgb, dtype=tf.uint8)

# Add dims to rgb_tensor
rgb_tensor = tf.expand_dims(rgb_tensor , 0)

#===load model and labels=====#
detector = hub.load("https://tfhub.dev/tensorflow/efficientdet/lite2/detection/1")

# Loading csv with labels of classes
labels = pd.read_csv('resources/templates/csv/labels.csv', sep=';', index_col='ID')
labels = labels['OBJECT (2017 REL.)']

# ===Creating prediction====#
boxes, scores, classes, num_detections = detector(rgb_tensor)

# Processing outputs
pred_labels = classes.numpy().astype('int')[0]
pred_labels = [labels[i] for i in pred_labels]
pred_boxes = boxes.numpy()[0].astype('int')
pred_scores = scores.numpy()[0]

# Putting the boxes and labels on the image
for score, (ymin,xmin,ymax,xmax), label in zip(pred_scores, pred_boxes, pred_labels):
    if score < 0.5:
        continue

    score_txt = f'{100 * round(score)}%'
    img_boxes = cv2.rectangle(rgb,(xmin, ymax),(xmax, ymin),(0,255,0),2)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img_boxes, label,(xmin, ymax-10), font, 1.5, (255,0,0), 2, cv2.LINE_AA)
    cv2.putText(img_boxes,score_txt,(xmax, ymax-10), font, 1.5, (255,0,0), 2, cv2.LINE_AA)
# display image with object detection
plt.imshow(img_boxes)