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

out_path = "./test/"

# path, dirs, files = next(os.walk ("../done/Annotations/"))
# image_id = len(files) + 1
image_id = 1
for file_xml in files_xml:
    file_name = os.path.basename(file_xml)
    in_file = open(xml_path+file_name)
    tree=ET.parse(in_file)
    root = tree.getroot()
    # path = root.find('path').text
    name = root.find('filename').text
    path = "../done/JPEGImages/"+name
    img = cv2.imread(path)

    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        xmlbox = obj.find('bndbox')
        x = int(xmlbox.find('xmin').text)
        y = int(xmlbox.find('ymin').text)
        x1 = int(xmlbox.find('xmax').text)
        y1 = int(xmlbox.find('ymax').text)
        height = x1 - x
        width = y1 - y
        while height != width:
            if width < height:
                if y > 0:
                    y -= 1
                elif y1 < h:
                    y1 += 1
            elif width > height:
                if x > 0:
                    x -= 1
                elif x1 < w:
                    x1 += 1
            if (height != x1 - x) or (width != y1 - y):
                width = y1 - y
                height = x1 -x
            else:
                break
        if width != height:
            if width > height:
                y += 1
                width = y1 - y
            elif height > width:
                x += 1
                height = x1 -x
	    # x,y top left, x1,y1 bottom right
        cropped = img[y:y1,x:x1]
        cv2.imwrite(out_path+"%06d"%image_id+".jpg",cropped)
        image_id += 1