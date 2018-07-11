#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import cv2
import numpy as np
import os
import sys

name_file_input = sys.argv[1]
output_path = "../new/picture/"

cap = cv2.VideoCapture(name_file_input)

try:
    if not os.path.exists(output_path):
        os.makedirs(output_path)
except OSError:
    print ('Error: Creating directory of data')


from_frame = 0
count_frame = 1 #default
path, dirs, files = next(os.walk ("../new/picture/"))
image_id = len(files) + 1

while(True):
    ret, frame = cap.read()
    if count_frame > from_frame:
        cv2.imshow('image',frame)
        key = cv2.waitKey(0) & 0xff
        if key == ord("q"):
            continue
        elif key == 32:
            name = output_path + "%06d" % image_id + '.jpg'
            image_id += 1
            print ('Creating...' + name + ', in frame: ' + str(count_frame))
            cv2.imwrite(name, frame)
    count_frame +=1

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
