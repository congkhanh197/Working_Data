# Create image:
- Choose picture from video:

Run script:
```sh
cd script/
python choose_frame.py <name_of_file_input>
```
Press any key to go next frame, press space to choose image.
- Crop new picture:

Use `labelImg` to choose where to crop.
Run script:
```sh
cd script/
python get_new_image.py
```
- Create new lable:

Use `labelImg` to create new region.
Run script to take `.txt` label.
```sh
cd script/
python lable.py
```


./darknet detector demo ~/data_khanh/config/obj.data ~/data_khanh/config/yolov3-tiny.cfg ~/data_khanh/backup/yolov3-tiny_10000.weights ~/data_khanh/test.mp4
