# This script check in the xml_path folder, it check if there are any missing file from 000001.xml to num_file.xml
import os
import glob

xml_path = "../new/anno_picture/"
num_file = 650
files_xml = glob.glob(xml_path + "*.xml")
list_name = []
for file_xml in files_xml:
    file_name = os.path.basename(file_xml)
    list_name.append(file_name)

for x in range(1, num_file + 1):
    st = "%06d" %x + ".xml"
    if st not in list_name:
        print(st)
        break