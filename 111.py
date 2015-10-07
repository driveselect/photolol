from time import sleep, time
from SimpleCV import Camera, Image, Display
import os, sys
myCamera = Camera(prop_set={'width': 320, 'height': 240})
md = Display(resolution=(320, 240))
stache = Image("mustache.png")
def mustachify(frame):
    faces = frame.findHaarFeatures('face')
    if faces:
        for face in faces:
            print "Face at: " + str(face.coordinates())
            myFace = face.crop()
            noses = myFace.findHaarFeatures('nose')
            if noses:
                nose = noses.sortArea()[-1]
                print "Nose at: " + str(nose.coordinates())
                xmust = (face.points[0][0] + nose.x +
                     (stache.width / 2))
                ymust = (face.point5[0][1] + nose.y +
                         (stache.height / 3))
            else:
                return frame
        frame = frame.blit(stache, pos=(xmust, ymust), mask=stacheMask)
        return frame
    else:
        return frame
while 1:
    stacheMask = stache.createBinaryMask(color1=(0,0,0), color2=(254,254,254))
    stacheMask = stacheMask.invert()
    print ("press 1 key to cont. or any key to exit")
    p2 = input()

    frame = myCamera.getImage()
    if p2 == 1:
        frame = mustachify(frame)
        frame.save("228" + ".jpg")
        frame = frame.flipHorizontal()
        execfile('1.py')
    else:
        print ("exiting")
        sleep (1)
        sys.exit()
