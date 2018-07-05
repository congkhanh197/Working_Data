import xml.etree.ElementTree as ET
import pickle
import os
import glob
from os import listdir, getcwd
from os.path import join



# for data_set, image_set in sets:
#     image_ids = open('data/%s/ImageSets/Main/%s.txt'%(data_set, image_set)).read().strip().split()
#     for image_id in image_ids:
#         convert_annotation(data_set,image_id)

motorbike = 0
car_s = 0
car_l = 0
walker = 0
bicycle = 0
orther = 0

xml_path = "../done/Annotations/"
files_xml = glob.glob(xml_path + "*.xml")
image_id = 813
count_file = 0
for file_xml in files_xml:
    count_file += 1
    file_name = os.path.basename(file_xml)
    in_file = open(xml_path+file_name)
    tree=ET.parse(in_file)
    root = tree.getroot()
    path = root.find('path').text
    for obj in root.iter('object'):
        if obj.find('name').text == 'motorbike':
            motorbike +=1
        elif obj.find('name').text == 'car_s':
            car_s += 1
        elif obj.find('name').text == 'car_l':
            car_l += 1
        elif obj.find('name').text == 'walker':
            walker += 1
        elif obj.find('name').text == 'bicycle':
            bicycle += 1
        else: 
            orther += 1

print('count_file', count_file)
print('motorbike', motorbike)
print('car_s', car_s)
print('car_l', car_l)
print('walker', walker)
print('bicycle', bicycle)


        

