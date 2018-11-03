#!/usr/bin/python

import io
import os
# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/pi/squirrelcred.json"

# Instantiates a client
client = vision.ImageAnnotatorClient()
# The name of the image file to annotate
# file_name = os.path.join(
#     os.path.dirname(__file__),
#     'resources/wakeupcat.jpg')

# Loads the image into memory
# with io.open(file_name, 'rb') as image_file:
#     content = image_file.read()
# image = types.Image(content=content)

def SpotObject(image, tag, confidence):
    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations

    print('Labels:')
    for label in labels:
        #if((label.description == tag) and (label.score > confidence):
        print(label.description, label.score)
        #return(true)
    return(False)
