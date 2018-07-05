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


xml_path = "../anno_picture/"
files_xml = glob.glob(xml_path + "*.xml")

path, dirs, files = next(os.walk ("../done/Annotations/"))
image_id = len(files) + 1
for file_xml in files_xml:
    file_name = os.path.basename(file_xml)
    in_file = open(xml_path+file_name)
    tree=ET.parse(in_file)
    root = tree.getroot()
    path = root.find('path').text
    img = cv2.imread(path)

    for obj in root.iter('object'):
        # print(path)
        xmlbox = obj.find('bndbox')
        x = int(xmlbox.find('xmin').text)
        y = int(xmlbox.find('ymin').text)
        x1 = int(xmlbox.find('xmax').text)
        y1 = int(xmlbox.find('ymax').text)
	# x,y top left, x1,y1 bottom right
        cropped = img[y:y1,x:x1]
        cv2.imwrite('../JPEG/'+"%06d"%image_id+".jpg",cropped)
        image_id += 1
