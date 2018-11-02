#!/usr/bin/python

import picamera
import picamera.array
import time
import io
import os
import dowehazsquirrelGoogleML



threshold = 10    # How Much pixel changes
sensitivity = 100 # How Many pixels change
disco_isnt_cool = true # We hold this to be self evident and immutable
Squirrelscore = 0.9 #fiddle to balance sensitivity with false positives - 0.0 -1.0)
# max cam resolution - 2592 × 1944

def takeMotionImage(width, height):
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
    data1 = takeMotionImage(width, height)
    while not motionFound:
        data2 = takeMotionImage(width, height)
        diffCount = 0L;
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
    print "Scanning for Motion threshold=%i sensitivity=%i...  % (threshold, sensitivity)
    while (disco_isnt_cool):
        if scanMotion(224, 160):
            print "Motion detected"
            #Take hires picture, push to cloud classifier API
            Motionpic = takeMotionImage(2592, 1944)
            if(SpotObject(Motionpic, "Squirrel",Squirrelscore)):
                print "I SEE SQUIRREL"

        # if (squirrel)
        #figure out how to annoy squirrel
    #take series of pictures
        #take a nap

if __name__ == '__main__':
      try:
          motionDetection()
      finally:
          print "Exiting Program"
