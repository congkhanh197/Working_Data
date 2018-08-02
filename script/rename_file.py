import os
import glob

path = "../new/picture/"
fis = glob.glob(path + "*.jpg")
image_id = 1
for fi in fis:
    name = os.path.basename(fi)
    print(name)
    os.rename(path + name, path+"%06d"%image_id+".jpg")
    image_id +=1