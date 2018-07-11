import xml.etree.ElementTree as ET
import pickle
import os
import glob
from os import listdir, getcwd
from os.path import join
import cv2
xml_path = "../new/new_picture_new_video/"
files_xml = glob.glob(xml_path + "*.jpg")
image_id = 750
list_name = []
for file_xml in files_xml:
    file_name = os.path.basename(file_xml)
    img = cv2.imread(xml_path+file_name)
    cv2.imwrite(xml_path+"%06d"%image_id+".jpg",img)
    image_id += 1
