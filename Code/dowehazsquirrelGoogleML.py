#!/usr/bin/python

import io
import os
# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/pi/squirrelcred.json"



def SpotObject(ImageBytesIO, tag, confidence):
    # Performs label detection on the content file (io.ByteIO), tag to search for, confidence required for match

    # Instantiates a client
    client = vision.ImageAnnotatorClient()

    # copies the image into memory
    content = ImageBytesIO.read()
    print('content type=',type(content))
    image = vision.types.Image(content=content)
    print('image type=',type(image))

    response = client.label_detection(image=image)
    
    labels = response.label_annotations

    print('Labels:')
    for label in labels:
        #if((label.description == tag) and (label.score > confidence):
        print(label.description, label.score)
        #return(true)
    return(False)# Instantiates a client
