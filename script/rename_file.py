import os
import glob

path = "/home/nam/data/fd/"
fis = glob.glob(path + "*.jpg")
image_id = 1
for fi in fis:
    name = os.path.basename(fi)
    os.rename(path + name, path+"%06d"%image_id+".jpg")
    image_id +=1