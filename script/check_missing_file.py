import xml.etree.ElementTree as ET
import pickle
import os
import glob
from os import listdir, getcwd
from os.path import join
import cv2


# for data_set, image_set in sets:
#     image_ids = open('data/%s/ImageSets/Main/%s.txt'%(data_set, image_set)).read().strip().split()
#     for image_id in image_ids:
#         convert_annotation(data_set,image_id)


xml_path = "../done/Annotations/"
files_xml = glob.glob(xml_path + "*.xml")
image_id = 1
list_name = []
for file_xml in files_xml:
    file_name = os.path.basename(file_xml)
    list_name.append(file_name)
    # in_file = open(xml_path+file_name)
    # if file_name != ("%06d" %image_id):
    #     print(file_name)
    #     break
    # image_id += 1

for x in range(1, 3458):
    st = "%06d" %x + ".xml"
    if st not in list_name:
        print(st)
        break