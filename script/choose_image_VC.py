#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import cv2
import numpy as np
import os
import sys

# add name_file_input as parameter
name_file_input = sys.argv[1]
output_path = "../data/test/"

cap = cv2.VideoCapture(name_file_input)

try:
    if not os.path.exists(output_path):
        os.makedirs(output_path)
except OSError:
    print ('Error: Creating directory of data')



count_frame = 1 #const
path, dirs, files = next(os.walk ("../new/picture/"))
image_id = len(files) + 1


# fourcc = cv2.VideoWriter_fourcc('X','2','6','4')

# out = cv2.VideoWriter('/tmp/output.mp4',fourcc, 20.0, (640,480))
# fourcc = cv2.VideoWriter_fourcc(*'XVID') 
video = cv2.VideoWriter('test.mp4',0x00000021,13,(839,463))

while(True):
    ret, frame = cap.read()
    # x,y top left; x1,y1 bottom right;
    # cropped = frame[y:y1,x:x1]
    cropped = frame[257:720,97:936]
    if count_frame % 250 == 0:
        name = output_path + "%06d" % image_id + '.jpg'
        image_id += 1
        print ('Creating...' + name + ', in frame: ' + str(count_frame))
        cv2.imwrite(name, cropped)
    video.write(cropped)
    count_frame +=1

# When everything done, release the capture
cap.release()
video.release()
cv2.destroyAllWindows()