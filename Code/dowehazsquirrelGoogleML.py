#!/usr/bin/python

import io
import os
import sys
from google.cloud import vision
from google.cloud.vision import types
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/pi/squirrelcred.json"



def SpotObject(ImageBytesIO, tag, confidence):
    # Performs label detection on the content file (io.ByteIO), tag to search for, confidence required for match
    # Instantiates a client
    client = vision.ImageAnnotatorClient()
    # copies the image into memory
    #print('ImageBytesIO type=',type(ImageBytesIO),'    ',sys.getsizeof(ImageBytesIO))

    ImageBytesIO.seek(0)
    content = ImageBytesIO.read()
    #print('content type=',type(content),'    ',sys.getsizeof(content))

    image = vision.types.Image(content=content)
    #print('image type=',type(image),'    ',sys.getsizeof(image))

    response = client.label_detection(image=image, maxResults=20)
    labels = response.label_annotations

    for label in labels:
        print(label.description, label.score)
        if((label.description == tag)):   #and (label.score > confidence)):
            print('FOUND IT!!-----------------------------------------')
            #print(label.description, label.score)
            return(True)
    return(False)
