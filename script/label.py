import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join
import glob


classes = ["motorbike", "car_s", "car_l", "bicycle", "walker"]

def convert(size, box):
    dw = 1./(size[0])
    dh = 1./(size[1])
    x = (box[0] + box[1])/2.0 - 1
    y = (box[2] + box[3])/2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

xml_path = "../done/Annotations/"
files_xml = glob.glob(xml_path + "*.xml")
image_id = 0
count_file = 0
for file_xml in files_xml:
    count_file += 1
    file_name = os.path.basename(file_xml)
    in_file = open(xml_path+file_name)
    image_id, extension = os.path.splitext(file_name)
    out_file = open('../done/labels/%s.txt'%(image_id), 'w')
    tree=ET.parse(in_file)
    root = tree.getroot()
    path = root.find('path').text
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult)==1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w,h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')


list_file = open('../config/train.txt', 'w')
path, dirs, files = next(os.walk ("../done/JPEGImages/"))
num_image= len(files) + 1
for image_id in range(1,num_image):
    list_file.write('/home/khanh/data_khanh/done/JPEGImages/'+'%06d'%image_id+'.jpg\n')
list_file.close()
os.system('cp ../config/train.txt ../config/test.txt')