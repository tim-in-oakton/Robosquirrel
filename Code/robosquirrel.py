#!/usr/bin/python

import picamera
import picamera.array
import time
import io
import os
import sys # for sizeof
from dowehazsquirrelGoogleML import SpotObject #we'll use different models - cloud, hybrid, edge
from annoysquirrel import annoySquirrelOn, annoySquirrelOff

threshold = 45    # How Much pixel changes
sensitivity = 400 # How Many pixels change
disco_isnt_cool = True # We hold this to be self evident and immutable
Squirreltag = "squirrel"
Squirrelscore = 0.5 #fiddle to balance sensitivity with false positives - 0.0 -1.0)
# max cam resolution - 2592 × 1944

def takeMotionImage(width, height):
        with picamera.PiCamera() as camera:
            streamPic = io.BytesIO()
            time.sleep(1)
            camera.resolution = (width, height)
            with picamera.array.PiRGBArray(camera) as stream:
                camera.exposure_mode = 'auto'
                camera.awb_mode = 'auto'
                camera.capture(streamPic, 'jpeg')
                return streamPic

        # #time.sleep(1)
        # # Create an in-memory stream
        # streamPic = io.BytesIO()
        # camera = picamera.PiCamera()
        # camera.start_preview()
        # # Camera warm-up time
        # time.sleep(2)
        # camera.capture(streamPic, 'jpeg')
        # camera.close()
        # return streamPic

def takeMotionImageArray(width, height):
    with picamera.PiCamera() as camera:
        time.sleep(1)
        camera.resolution = (width, height)
        with picamera.array.PiRGBArray(camera) as stream:
            camera.exposure_mode = 'auto'
            camera.awb_mode = 'auto'
            camera.capture(stream, format='rgb')
            return stream.array

def scanMotion(width, height):
    motionFound = False
    data1 = takeMotionImageArray(width, height)
    while not motionFound:
        data2 = takeMotionImageArray(width, height)
        diffCount = 0;
        for w in range(0, width):
            for h in range(0, height):
                # get the diff of the pixel. Conversion to int
                # is required to avoid unsigned short overflow.
                diff = abs(int(data1[h][w][1]) - int(data2[h][w][1]))
                if  diff > threshold:
                    diffCount += 1
            if diffCount > sensitivity:
                break;
        if diffCount > sensitivity:
            motionFound = True
        else:
            data2 = data1
    return motionFound

def motionDetection():
    print ("Scanning for Motion")
    while (disco_isnt_cool):
        if scanMotion(224, 160):
            print ("Motion detected")
            #Take hires picture, push to cloud classifier API
            Motionpic = takeMotionImage(1024, 768)
            #print ("tookMotionImage - sending to Google")
            #print('Motionpic type is',type(Motionpic),'    ',sys.getsizeof(Motionpic))

            if(SpotObject(Motionpic, Squirreltag ,Squirrelscore)):
                print ("I SEE A SQUIRREL")
                #annoy squirrel - IFTT and Smart Life interaction - Webhooks
                annoySquirrelOn()
                for x in range(1,4): #take 3 pics
                    filename = '../Squirrelpic-%s.jpg'%time.strftime("%Y%m%d-%H%M%S")
                    print('filename is',filename)
                    f = open(filename,'wb')
                    Motionpic.seek(0)
                    f.write(Motionpic.read())
                    f.close()
                    Motionpic = takeMotionImage(1024, 768)
                    annoySquirrelOff()


            #print ("no squirrel now")
            #time.sleep(1)


if __name__ == '__main__':
      try:
          motionDetection()
      finally:
          print ("Exiting Program")
