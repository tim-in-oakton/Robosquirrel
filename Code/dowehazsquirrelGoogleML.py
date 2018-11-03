#!/usr/bin/python

import io
import os
import sys
# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/pi/squirrelcred.json"



def SpotObject(ImageBytesIO, tag, confidence):
    # Performs label detection on the content file (io.ByteIO), tag to search for, confidence required for match

    # Instantiates a client
    client = vision.ImageAnnotatorClient()

    # copies the image into memory
    print('ImageBytesIO type=',type(ImageBytesIO),'    ',sys.getsizeof(ImageBytesIO))
    # says ImageBytesIO type= <class '_io.BytesIO'>      678706

    #fakefile = open(ImageBytesIO,'r')
    ImageBytesIO.seek(0)
    content = ImageBytesIO.read()
    print('content type=',type(content),'    ',sys.getsizeof(content))
    # says content type= <class 'bytes'>      678657

    image = vision.types.Image(content=content)
    print('image type=',type(image),'    ',sys.getsizeof(image))
    #says image type= <class 'google.cloud.vision_v1.types.Image'>      60

    response = client.label_detection(image=image)
    labels = response.label_annotations

    print('Labels:')
    for label in labels:
        #if((label.description == tag) and (label.score > confidence):
        print(label.description, label.score)
        #return(true)
    return(False)# Instantiates a client
