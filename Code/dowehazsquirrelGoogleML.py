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

    #read the passed ByteIO image into content
    ImageBytesIO.seek(0)
    content = ImageBytesIO.read()
    # load the image into a vision.types image
    image = vision.types.Image(content=content)

    # Build and make the request on Google w features
    label_detection_feature = {
        'type': vision.enums.Feature.Type.LABEL_DETECTION, 'max_results': 20}
    request_features = [label_detection_feature]
    response = client.annotate_image(
        {'image': image, 'features': request_features})

    # another working approach, no features
    #response = client.label_detection(image=image)

    #load labels with the annotated label responses returned
    labels = response.label_annotations

    for label in labels:
        #print("          ",label.description, label.score)
        if((label.description == tag)):   #and (label.score > confidence)):
            print(label.description, label.score)
            return(True)
    return(False)
